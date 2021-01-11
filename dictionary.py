# def main():
#     dictionary = {
#         1: 11,
#         2: 22,
#         3: 33,
#     }

#     print(dictionary[2])


def test():
    populationCountries = {
        'country1': 1,
        'country2': 2,
        'country3': 3,
    }

    for country in populationCountries.keys():
        print(country)

    for country in populationCountries.values():
        print(country)

    for country, population in populationCountries.items():
        print(country + ': ' + str(population))


if __name__ == "__main__":
    # main()
    test()
