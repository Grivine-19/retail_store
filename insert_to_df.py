def insert_to_df(self, original_df, new_df):
        '''
        Insert new data into an existing dataframe.
        
        Args:
            original_df(DataFrame) : DataFrame with data from the first page of a product.
            new_df(DataFrame) : DataFrame with data from other pages. 
            
        Returns:
            original_df(DataFrame) : DataFrame with data from original_df + new_df.
        '''
        
        self.original_df = original_df
        self.new_df = new_df
        
        # Insert new data into the DataFrame of the first page
        original_df = original_df.append(new_df,ignore_index=True, verify_integrity = True)

        return original_df