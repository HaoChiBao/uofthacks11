import cohere

api = cohere.Client("pdm3fybwqkzCV5BkUhptIesobKyqZvpMmnmteNvZ")

def grabTasks(topic):
    generate = api.chat(
        model="command-nightly",
        message=f"Strictly provide a list of 1 to 2 short routine tasks that a student can perform to enhance their understanding of the topic '{topic}'. These tasks should boost productivity and contribute to a better grasp of the material. Strictly give them to me in the form of ['task1','task2'] and no other format."
    )

    print(generate.text)

    strip_1 = generate.text.strip("[]")

    tasks = strip_1.split(',')
    
    tasks = [task.strip().strip("'") for task in tasks]
    return tasks


user_input = input("Enter a topic: ")
tasks = grabTasks(user_input)