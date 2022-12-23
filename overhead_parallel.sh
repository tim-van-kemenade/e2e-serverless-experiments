#!/bin/bash

mkdir -p data

for i in {1..20} ; do
#    echo -n "" > data/overhead_parallel_"${i}".txt
    fetchArray=()
    for ((j=1;j<=i;j++))
    do
        fetchArray+=(-o data/aatmp_$"{i}"_$"{j}".txt "http://127.0.0.1:8080/function/overhead")
    done
    curl -w "@curl-format.txt" -s -Z "${fetchArray[@]}" #>> overhead_parallel_"${i}".txt
done

#PODNAME=$(kubectl get pod -n openfaas-fn | sed -n "s/\(${podname}-[^ ]*\)\(.*\)/\1/gp" | tr '\n' ' ')
#kubectl logs -n openfaas-fn $PODNAME > data/pod_log_4.txt
