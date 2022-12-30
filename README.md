# producthunt-scraper 🕸

Set of basic script python scripts to fetch data from [Product Hunt](https://www.producthunt.com/) and analyze it.

## Fetching

In both the scripts - `product-fetcher.py` and `product-fetcher-async.py` you can edit -

```py
# start_date

start_date = {
    "year": 2022,
    "month": 1,
    "day": 1,
}

# end_date
end_date = {
    "year": 2022,
    "month": 1,
    "day": 15,
}


```

to change the date range for which you want to fetch the data.

A sample run would look something like this -

```terminal
python product-fetcher.py                                                                             ─╯
2022-01-01
2022-01-02
2022-01-03
2022-01-04
...
2022-01-15
Time taken to run the script: 5.975425720214844 seconds
```

After that, you can run the script using `python product-fetcher.py` or `python product-fetcher-async.py` depending on which script you want to run. This will crate a file `products.csv` in the same directory which will contain the data.

## Analyzing

Once you have the data, you can run the `product-analyzer.py` script to analyze the data after setting correct path to the `products.csv` file in the script.

This script will output analysis in the terminal.

```terminal
Product with highest votes: Fitmint with 6781 votes
Product with most comments: Via Protocol with 2257 comments
topic_name
Productivity         2262
Android               796
Design Tools          782
Web App               475
iOS                   338
Chrome Extensions     320
Developer Tools       310
Marketing             278
Fintech               242
Health & Fitness      198
...(more analysis)
```

## Notes

- These scripts were never meant to be published, so they might not be the best code. If you have any suggestions, feel free to open an issue or a PR.

- this was used to create this twitter thread - [ProductHunt Recap 2022](https://twitter.com/toughyear/status/1608787504764973056)

Ciao! 🤙
