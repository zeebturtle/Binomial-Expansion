base = 2
n = 0.5

#I was designing this scaling loop to get base_scaled as close to 1 as possible so that convergence speed can be maximised.
#I'm aware that this can be done more simply, so I'm not using this code. It's also a bloody nightmare trying to keep track of everything using this code.
base_scaled = base

count = 0

interval_set = {base_scaled}

interval_list = [base_scaled]

scaling_complete = False

while base_scaled >= 2:
    base_scaled /= 4

    interval_set.add(base_scaled)

    interval_list.append(base_scaled)

    count += 1

while not scaling_complete:

    while base_scaled < 1:

        base_scaled *= 4

        interval_set.add(base_scaled)

        interval_list.append(base_scaled)

        if len(interval_list) != len(interval_set):
            base_scaled = min(interval_set, key=lambda x: abs(x - 1))

            scaling_complete = True

            break

        count -= 1

    if base_scaled == 1:
        break

    if scaling_complete == True:
        break

    while base_scaled > 1:

        base_scaled /= 4

        interval_set.add(base_scaled)

        interval_list.append(base_scaled)

        if len(interval_list) != len(interval_set):
            base_scaled = min(interval_set, key=lambda x: abs(x - 1))

            scaling_complete = True

            break

        count += 1

    if scaling_complete == True:
        break

    if base_scaled == 1:
        break

    # End of scaling loop part 2