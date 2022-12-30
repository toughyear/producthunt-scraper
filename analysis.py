import pandas as pd

df = pd.read_csv("products_async_full.csv")


# > head -3 products_async.csv                                                                            ─╯
# id,name,slug,tagline,shortenedUrl,commentsCount,createdAt,featuredAt,updatedAt,pricingType,topic_id,topic_name,topic_slug,redirectToProduct_id,redirectToProduct_slug,disabledWhenScheduled,votesCount,productState,thumbnailImageUuid
# 325054,World Explorer by Insured Nomads,world-explorer-by-insured-nomads,Insurance meets travel tech for the global work revolution,/r/p/325054,84,2022-01-01T00:12:52-08:00,2022-01-01T00:12:52-08:00,2022-12-24T09:50:42-08:00,,249,Global Nomad,global-nomad,119745,insured-nomads,True,389,default,9bc773c8-1720-45b6-86f3-75d257338bc3.png
# 325075,Tailwind Box Shadows,tailwind-box-shadows,Curated list of box shadows for your cards to stand out,/r/p/325075,25,2022-01-01T02:40:32-08:00,2022-01-01T02:40:32-08:00,2022-12-21T09:16:59-08:00,free,46,Productivity,productivity,472948,tailwind-box-shadows,True,203,default,f182991d-f034-43b8-8672-c5ec338ba09d.png


def highest_voted_product(df):
    df = df.sort_values("votesCount", ascending=False)
    highest_vote_product = df.iloc[0]
    print(
        f"Product with highest votes: {highest_vote_product['name']} with {highest_vote_product['votesCount']} votes"
    )


def most_commented_product(df):
    df = df.sort_values("commentsCount", ascending=False)
    most_commented_product = df.iloc[0]
    print(
        f"Product with most comments: {most_commented_product['name']} with {most_commented_product['commentsCount']} comments"
    )


def top_10_topics(df):
    top_df = df.groupby("topic_name").size().sort_values(ascending=False).head(10)
    print(top_df)


def top_20_words_in_tagline(df):
    hash_table = {}

    for tagline in df["tagline"]:
        words = tagline.split(" ")
        for word in words:
            if word in hash_table:
                hash_table[word] += 1
            else:
                hash_table[word] = 1

    sorted_hash_table = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)
    # remove if count is <=5
    sorted_hash_table = [x for x in sorted_hash_table if x[1] > 150]

    print(sorted_hash_table)


def dates_with_most_and_least_products(df):
    hash_table = {}

    for date in df["createdAt"]:
        date = date.split("T")[0]
        if date in hash_table:
            hash_table[date] += 1
        else:
            hash_table[date] = 1

    sorted_hash_table = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)

    print("Date with most products: ", sorted_hash_table[0])
    print("Date with least products: ", sorted_hash_table[-1])


def total_products(df):
    print("Total products: ", len(df))


def pricing_options_distribution(df):
    pricing_options = df.groupby("pricingType").size()

    print(pricing_options)

    # print % of total products
    for index, value in pricing_options.items():
        print(f"{index} %: {value / len(df) * 100}")


def comments_per_month(df):
    """prints list of comments per month, sorted by month (2022-01-01T00:12:52-08:00 is the format)"""
    hash_table = {}

    for date in df["createdAt"]:
        date = date.split("T")[0]
        month = date.split("-")[1]
        if month in hash_table:
            hash_table[month] += 1
        else:
            hash_table[month] = 1

    sorted_hash_table = sorted(hash_table.items(), key=lambda x: x[0])

    print("Comments per month: ", sorted_hash_table)


def product_with_most_comments_per_vote(df):
    """prints product with most comments per vote"""
    df["comments_per_vote"] = df["commentsCount"] / df["votesCount"]
    df = df.sort_values("comments_per_vote", ascending=False)
    most_commented_product_per_vote = df.iloc[0]
    print(
        f"Product with most comments per vote: {most_commented_product_per_vote['name']} with {most_commented_product_per_vote['comments_per_vote']} comments per vote"
    )


def product_with_largest_difference_between_create_and_update_date(df):
    """prints product with largest difference between create and update date"""
    df["create_date"] = pd.to_datetime(df["createdAt"])
    df["update_date"] = pd.to_datetime(df["updatedAt"])
    df["time_diff"] = df["update_date"] - df["create_date"]
    df = df.sort_values("time_diff", ascending=False)
    largest_diff = df.iloc[0]
    print(
        f"Product with largest difference between create and update date: {largest_diff['name']} with {largest_diff['time_diff']} time difference"
    )


def month_with_most_launches(df):
    """prints month with most launches"""
    hash_table = {}

    for date in df["createdAt"]:
        date = date.split("T")[0]
        month = date.split("-")[1]
        if month in hash_table:
            hash_table[month] += 1
        else:
            hash_table[month] = 1

    sorted_hash_table = sorted(hash_table.items(), key=lambda x: x[1], reverse=True)

    print("Month with most launches: ", sorted_hash_table[0])


def find_correlation_between_tagline_and_votes(df):
    """prints correlation between tagline and votes"""
    df["tagline_length"] = df["tagline"].str.len()
    df["tagline_length"].fillna(0, inplace=True)
    df["tagline_length"] = df["tagline_length"].astype(int)
    df["votesCount"] = df["votesCount"].astype(int)
    print(
        "correlation between tagline and votes: ",
        df["tagline_length"].corr(df["votesCount"]),
    )


def find_corr_between_comments_and_votes(df):
    """prints correlation between comments and votes"""
    df["commentsCount"] = df["commentsCount"].astype(int)
    df["votesCount"] = df["votesCount"].astype(int)
    print(
        "correlation between comments and votes: ",
        df["commentsCount"].corr(df["votesCount"]),
    )


def average_votes_and_comments_for_top_10_topics(df):
    """prints average votes and comments for top 10 topics"""
    top_df = df.groupby("topic_name").size().sort_values(ascending=False).head(10)
    top_topics = top_df.index
    df = df[df["topic_name"].isin(top_topics)]
    print("Average votes and comments for top 10 topics: ")
    print(df.groupby("topic_name")[["votesCount", "commentsCount"]].mean())


def highest_average_votes_and_comments_for_a_topic(df):
    """prints highest average votes and comments for a topic"""
    df = df.groupby("topic_name")[["votesCount", "commentsCount"]].mean()
    df = df.sort_values(by=["votesCount", "commentsCount"], ascending=False)
    print("Highest average votes and comments for a topic: ")
    print(df.head(10))


# call the function
highest_voted_product(df)
most_commented_product(df)
top_10_topics(df)
top_20_words_in_tagline(df)
dates_with_most_and_least_products(df)
total_products(df)
pricing_options_distribution(df)
comments_per_month(df)
product_with_most_comments_per_vote(df)
product_with_largest_difference_between_create_and_update_date(df)
month_with_most_launches(df)
find_correlation_between_tagline_and_votes(df)
find_corr_between_comments_and_votes(df)
average_votes_and_comments_for_top_10_topics(df)
highest_average_votes_and_comments_for_a_topic(df)
