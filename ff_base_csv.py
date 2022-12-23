import re

function_times = []
curl_times = []
with open("data/ff-overhead.txt") as overhead_file:
    lines = overhead_file.readlines()
    for i in range(0, len(lines) - 1, 2):
        f_time = float(lines[i].split(" ")[-2])
        function_times.append(f_time)
        curl_times.append(float(lines[i + 1]))
function_times = function_times[-100:]
curl_times = curl_times[-100:]
max_f = max(function_times)
max_c = max(curl_times)

pod_times = []
with open("data/ff_pod_log.txt") as pod_log_file:
    for line in pod_log_file:
        if re.search("Duration:", line):
            pod_time = line.split()[-1][:-1]
            pod_times.append(float(pod_time))
            # print(pod_time)
pod_times = pod_times[-100:]
with open("csv/ff_data_line.csv", "w") as line_file:
    line_file.write("A,Call overhead,OpenFaaS overhead,Time inside function,Total time\n")
    for i in range(100):
        line_file.write(f"{i+1},{float(curl_times[i]) - float(pod_times[i])},{pod_times[i]},{function_times[i]},{curl_times[i]}\n")
with open("csv/ff_data_bar.csv", "w") as line_file:
    line_file.write("A,Call overhead,OpenFaaS overhead,Time inside function\n")
    for i in range(100):
        line_file.write(f"{i+1},{float(curl_times[i]) - float(pod_times[i])},{float(pod_times[i]) - function_times[i]},{function_times[i]}\n")
with open("csv/ff_data_boxplot.csv", "w") as boxplot_file:
    boxplot_file.write(f"A,{','.join([str(i + 1)for i in range(100)])}\n")
    overhead_time = []
    execution_pod_time = []
    execution_function_time = []
    total_time = []
    for i in range(100):
        overhead_time.append(str(float(curl_times[i]) - float(pod_times[i])))
        # execution_pod_time.append(str(float(pod_times[i])))float(curl_times[i]) - float(pod_times[i]
        execution_pod_time.append(str(float(curl_times[i]) - float(pod_times[i])))
        execution_function_time.append(str(float(function_times[i])))
        total_time.append(str(float(curl_times[i])))
    boxplot_file.write(f"Call overhead,{','.join(overhead_time)}\n")
    boxplot_file.write(f"OpenFaaS overhead,{','.join(execution_pod_time)}\n")
    boxplot_file.write(f"Time inside function,{','.join(execution_function_time)}\n")
    # boxplot_file.write(f"Total time,{','.join(total_time)}\n")
