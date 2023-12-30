print("---------------------------------------------------------------------------------------")
print("------------------------Python-Search-Engine-------------------------------------------")
print("---------------------------------------------------------------------------------------")
search_engine = input("Type And Enter to Search\n")
if search_engine == "World War Two" or search_engine == "world war two" or search_engine == "WW2":
    print("World War II or the Second World War, often abbreviated as WWII or WW2, ")
    print("was a global war that lasted from 1939 to 1945. ")
    print("t involved the vast majority of the world's countries")
    print("including all of the great powers—forming two opposing military alliances: the Allies and the Axis powers.")
    print("Dates: Sep 1, 1939 – Sep 2, 1945")
    print("Location: Europe, Africa and Asia")
elif search_engine == "Chinese Civil War" or search_engine == "chinese civil war":
    print("The Chinese Civil War was fought between the Kuomintang-led government of the Republic of China")
    print("and forces of the Chinese Communist Party, lasting intermittently after 1927.")
    print("Dates: Aug 1, 1927 – Dec 7, 1949")
    print("Location: Mainland China, Taiwan Strait")
elif search_engine == "Philippine American War" or search_engine == "philippine american war":
    print("The Philippine–American War or the Filipino–American War, ")
    print(" previously referred to as the Philippine Insurrection or the Tagalog Insurgency by the United States, ")
    print("was an armed conflict between the First Philippine Republic and the United States that started on")
    print("February 4, 1899, and ended on July 2, 1902.")
elif search_engine == "Russian Ukraine War" or search_engine == "russian ukraine war":
    print("The Russo-Ukrainian War,[18][d] also known as the Russia–Ukraine War, has been ongoing between Russia "
          "(alongside Russian separatists in Ukraine) and Ukraine since February 2014 Following "
          "Ukraine's Revolution of Dignity, Russia annexed Crimea from Ukraine and supported"
          " pro-Russian separatists in the war in Donbas against Ukrainian government forces;"
          " fighting for the first eight"
          " years of the conflict also included naval incidents, cyberwarfare, and heightened political tensions. "
          "Throughout 2021, bilateral tensions rose due to a Russian military buildup near the border with Ukraine, "
          "and on 24 February 2022, the conflict saw a major escalation "
          "as Russia launched a full-scale invasion of Ukraine.")
    print("Date: 20 February 2014 – present 8 years, 8 months, 2 weeks and 2 days")
    print("Location: rUkraine and Russia")
    print("Status - Ongoing")
    print("Territorial changes	Between 2014 and 2022: Annexation of Crimea"
          " by the Russian Federation Seizure of territory in eastern Ukraine by pro-Russia separatists"
          "Since 2022: "
          "Invasion of mainland Ukraine by Russia"
          "Annexation of southeastern Ukraine by the Russian Federation")

else:
    print("------------------------------------------------------------------------------------------")
    print("--------------------------------No-Data-Found---------------------------------------------")
    print("------------------------------------------------------------------------------------------")
user_input = ''

while True:
    user_input = input('Do you want to continue? yes/no: ')

    if user_input.lower() == 'yes':
        print("---------------------------------------------------------------------------------------")
        print("------------------------Python-Search-Engine-------------------------------------------")
        print("---------------------------------------------------------------------------------------")
        search_engine = input("Type And Enter to Search\n")
        if search_engine == "World War Two" or search_engine == "world war two" or search_engine == "WW2":
            print("World War II or the Second World War, often abbreviated as WWII or WW2, ")
            print("was a global war that lasted from 1939 to 1945. ")
            print("t involved the vast majority of the world's countries")
            print("including all of the great powers—forming two opposing military alliances:"
                  " the Allies and the Axis powers.")
            print("Dates: Sep 1, 1939 – Sep 2, 1945")
            print("Location: Europe, Africa and Asia")
        elif search_engine == "Chinese Civil War" or search_engine == "chinese civil war":
            print("The Chinese Civil War was fought between the Kuomintang-led government of the Republic of China")
            print("and forces of the Chinese Communist Party, lasting intermittently after 1927.")
            print("Dates: Aug 1, 1927 – Dec 7, 1949")
            print("Location: Mainland China, Taiwan Strait")
        elif search_engine == "Philippine American War" or search_engine == "philippine american war":
            print("The Philippine–American War or the Filipino–American War, ")
            print("previously referred to as the Philippine Insurrection or the Tagalog Insurgency by the United States")
            print("was an armed conflict between the First Philippine Republic and the United States that started on")
            print("February 4, 1899, and ended on July 2, 1902.")
        elif search_engine == "Russian Ukraine War" or search_engine == "russian ukraine war":
            print(
                "The Russo-Ukrainian War,[18][d] also known as the Russia–Ukraine War, has been ongoing between Russia "
                "(alongside Russian separatists in Ukraine) and Ukraine since February 2014 Following "
                "Ukraine's Revolution of Dignity, Russia annexed Crimea from Ukraine and supported"
                " pro-Russian separatists in the war in Donbas against Ukrainian government forces;"
                " fighting for the first eight"
                " years of the conflict also included naval incidents, "
                "cyberwarfare, and heightened political tensions. "
                "Throughout 2021, bilateral tensions rose due to"
                " a Russian military buildup near the border with Ukraine, "
                "and on 24 February 2022, the conflict saw a major escalation "
                "as Russia launched a full-scale invasion of Ukraine.")
            print("Date: 20 February 2014 – present 8 years, 8 months, 2 weeks and 2 days")
            print("Location: rUkraine and Russia")
            print("Status - Ongoing")
            print("Territorial changes	Between 2014 and 2022: Annexation of Crimea"
                  " by the Russian Federation Seizure of territory in eastern Ukraine by pro-Russia separatists"
                  "Since 2022: "
                  "Invasion of mainland Ukraine by Russia"
                  "Annexation of southeastern Ukraine by the Russian Federation")

        else:
            print("------------------------------------------------------------------------------------------")
            print("--------------------------------No-Data-Found---------------------------------------------")
            print("------------------------------------------------------------------------------------------")
        continue
    elif user_input.lower() == 'no':
        print('Close The Program')
        break
    else:
        print('Type yes/no')