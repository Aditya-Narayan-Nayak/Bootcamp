def get_scores(ball_and_score_list):
    ball_and_score_dict = {}
    for item in ball_and_score_list:
        pair = item.split(":")
        key, value = pair[0], int(pair[1])
        if key in ball_and_score_dict:
            score = ball_and_score_dict[key]
            ball_and_score_dict[key] = score + value
        else:
            ball_and_score_dict[key] = value
    return ball_and_score_dict
    
ball_score_list = input().split(",")
ball_score_pairs = get_scores(ball_score_list)
ball_score_items = ball_score_pairs.items()
ball_score_items = sorted(ball_score_items)
print(ball_score_items)
