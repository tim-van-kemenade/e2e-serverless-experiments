for j in range(20):
    calls = j + 1
    with open(f"data/overhead_parallel_{calls}.txt", "r") as read_file:
        for i in range(calls):
            with open(f"data/overhead_parallel_{calls}_{i + 1}.txt", "w") as write_file:
                write_file.write(read_file.readline())
                write_file.write(read_file.readline())
                write_file.write(read_file.readline())
