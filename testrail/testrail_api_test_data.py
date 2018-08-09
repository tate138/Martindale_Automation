import sys
sys.path.insert(0, '../glados/resources') # Import a module from other directory

import re
from testrail.testrail import testrail_api_glados


class testrail_api_test_data:
    def get_tables_from_testrail_data(self, case_id):
        '''
        Returns a list of tables detected from the testrail Data section.
        - The first row from the table is header row and identifies the values from test rows, other rows are representing test values

        Example:

        Table 1
        | auto_test_1 | col_name_2 | col_name_3 |
        | test_1 | value_1 | value_2 |
        | test_2 | value_3 | value_4 |

        Table 2
        | auto_test_2 | col_name_4 |
        | test_3 | value_3 |

        Example output:
        | [[
        |   {
        |     'auto_test_1': 'test_1',
        |     'col_name_2': 'value_1',
        |     'col_name_3': 'value_2'
        |   },
        |   {
        |     'auto_test_1': 'test_2',
        |     'col_name_2': 'value_3',
        |     'col_name_3': 'value_4'
        |   }
        | ],
        | [
        |   {
        |     'auto_test_2': 'test_3',
        |     'col_name_4': 'value_3'
        |   }
        | ]]

        Reference the testrail documentation on: http://docs.gurock.com/testrail-userguide/userguide-editor#tables
        '''
        # Get value from data field of the testrail test case
        tr_data = self._get_tr_custom_data_field(case_id)

        # In Data section there can be another lines of data wich are not part of the tables
        # Here every new row regardless of the type (table, link, text...) ends with "\r\n", except of the last in the section
        # The testrail table representation format in the response is:
        # ||| :Header1 | :Header2 | :Header3 | :Header4 \r\n || Value1 | Value2 | Value3 | Value4
        all_data_rows = tr_data.split("\r\n")

        # Extract only list of tables (if more than one) each table with a list of rows
        tables = []
        table = []
        # Iterate trough each row
        for row in all_data_rows:
            # Check for table rows
            # Each row that starts with, at least, two pipes is considered as table row
            if row.startswith('||'):
                # Remove the leading '||' from each table row by the regexp '^\|\|'
                table.append(re.sub('^\|\|', '', row))
            # Non-table Line: Append finished table to list
            # Once the row starts without '||', this means that this row is not part of a table
            elif table:
                # The table is finished and added in the tables list
                tables.append(table)
                # The last step is to empty the table list for eventual next one
                table = []
        # If last line was part of table, append last table
        if table:
            tables.append(table)

            # At the end of this proccess check if there is a table in tables list, stop further activity if there is no entry
        if not tables:
            raise(AssertionError("There are no tables in Data section in the test case: "+case_id))

        all_tables = []
        for table in tables:
            # Default: The first row is the table header row, others are table body rows
            header_row_values = table[0]
            body_rows_values = table[1:]

            # By conforming to the testrail best practices guideline, the first row of the table should always have '||' for each column.
            # This appears as '|||' when return from the "_get_tr_custom_data_field" function.
            # In such case there will be one pipe "|" at the beginning that needs to also be removed '^\|'
            # Split by delimiter of the new column "|"
            # This will result a list of all column names
            headers = re.sub('^\|', '', header_row_values).split('|')

            tbl_to_dict = []
            for row in body_rows_values:
                cells = row.split('|')
                tbl_row = {}
                for i in range(0, len(headers)):
                    # For each row (split logic as in heads), pair the column name with value in the row for the same position as column
                    # Append every pair in the table row list
                    # The testrail uses ":" as a alignment formater of the header text in the table
                    # So we need to remove the ":" from the beginning and/or the end head column name by the regexp '^:|:$'
                    header = re.sub('^:|:$', '', headers[i].strip())
                    tbl_row[header.strip()] = cells[i].strip()
                # Append every new row in the list of rows for the table, and return it
                tbl_to_dict.append(tbl_row)
            all_tables.append(tbl_to_dict)

        return all_tables

    def _get_tr_custom_data_field(self, case_id):
        '''
        Returns a content from Data section from testrail test case. Data section content is storred in "custom_data" from the response message
        Fails with a message if custom_data field is empty in the response
        '''
        # Get test case details in a format described in the testrail api documentation:
        # http://docs.gurock.com/testrail-api2/reference-cases#get_case section 'Response content'
        test_case = testrail_api_glados.get_test_case(case_id)
        # Get custom_data field which represents the content of the 'Data' section from the Testrail GUI
        tr_data = test_case['custom_data']
        if not tr_data:
            raise(AssertionError("There is no Data section in the test case: "+case_id))

        return tr_data


    def convert_tables_list_to_dictionary(self, tables_list):
        '''
            Format reference table page that is given from the testrail api output, and reformat to the following:
            - Dictionary containing all the tables on the page
            - Each Key is a tableName, Each Value is the coresponding table (in list format).
            - Each table (in list format) is a list of rows (in dictionary format).

            Example return:
            - { tableName: [ {Table1column1:row1value1, Table1column2:row1value2} , {Table1column1:row2value1}...], tableName : [ {Table1column1:row1value1} ,...] }

            Note:
           - This method only works for list of tables that contains a indexTable as the first table/element.
        '''

        # Dictionary to hold the new table dictionary
        tables_dic = {}

        # Grab the indexTable dictionary from the list of tables.
        ## The indexTable will always be the first table on the list/page.
        ## The indexTable only contains 1 row of data that is actually needed.
        indexTable = tables_list[0][0] # First row of the first table on the list

        # Match up each tableName to the corresponding table in the page using the indexTable dictionary
        for tableName, index in indexTable.items():
            # Add to the table dictionary with the 'tableName' and the corresponding table found in the page/list.
            tables_dic[tableName] = tables_list[int(index)]

        # Return the new table dictionary
        return tables_dic
