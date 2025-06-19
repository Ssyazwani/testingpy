
emoji_list = {
    ":1st_place_medal:": "🥇",
    ":money_bag:": "💰",
    ":smile_cat:": "😸",
    ":rocket:": "🚀",
    ":princess:": "👸",
   
}

user_input = input("Input: ").strip()


output = emoji_list.get(user_input, user_input)  # Return the input itself if not found


print("Output:", output)
