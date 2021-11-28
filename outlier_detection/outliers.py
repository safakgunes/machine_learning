def outlier(df):
        df_ = df.copy()
        df = df.drop('redundant data ',axis=1) #drop redundant data 

        q1 = df.quantile(0.25)
        q3 = df.quantile(0.75)

        iqr = q3 - q1

        lower_limit = q1 -(1.5 * iqr) 
        upper_limit = q3 +(1.5 * iqr)


        for col in df.columns:
            for i in range(0,len(df[col])):
                if df[col][i] < lower_limit[col]:            
                    df[col][i] = lower_limit[col]

                if df[col][i] > upper_limit[col]:            
                    df[col][i] = upper_limit[col]    


        for col in df.columns:
            df_[col] = df[col]

        return(df_)

new_data = outlier(Yours_Data)