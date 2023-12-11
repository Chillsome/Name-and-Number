import json
import pandas as pd
import os
def main():
    f = open('fis.json')
    j = json.load(f)
    my_dict = {}

    y = 0
    for i in j['data']:
        if 'isOktaGroup' in i:
            if i['isOktaGroup']:
                if 'FI Name' and 'FI Number' in i:
                    y += 1
                    my_dict[i['FI Name']] = i['FI Number']
                else:
                    if i['oktaDescription'][0].isdigit():
                        split = i['oktaDescription'].split(' ', 1)
                        y += 1
                        my_dict[split[1]] = split[0]
                    else:
                        continue
        else:
            continue
    f.close()
    df = pd.DataFrame(data=my_dict, index=[0])

    df = df.T

    print(df)
    directory = 'Names-Numbers'
    file = 'Fi_Names_and_Numbers.xlsx'

    if not os.path.exists(directory):
        os.makedirs(directory)
    df.to_excel(os.path.join(directory, file))



if __name__ == '__main__':
    main()

