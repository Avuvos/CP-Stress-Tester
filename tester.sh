# Compiling
g++ brute_sol.cpp -o brute_executable -std=c++17
g++ optimal_sol.cpp -o optimal_executable -std=c++17

# Getting the number of times to run the script from command line args
n=$1

RESET_COLOR="\x1b[0m"
AC_COLOR="\x1b[32m"
WA_COLOR="\x1b[31m"

declare -i ok=1

echo  -e "\nStarting to run $n testcases\n"

for ((testcase_number = 1; testcase_number <= n; testcase_number++)) do
    python testcase_generator.py # Generate and map testcases to testcase.txt
    # cat testcase.txt   If we want to print the testcase each time

    # Run the testcases on brute and optimal solutions
    ./brute_executable < testcase.txt > brute_out.txt
    ./optimal_executable < testcase.txt > optimal_out.txt

    # Check for diff in the output files
    if [[ $(diff brute_out.txt optimal_out.txt) ]]
    then
        echo -e "Test case $testcase_number: ${WA_COLOR}WRONG ANSWER${RESET_COLOR}"
        echo -e "\nInput:"
        cat testcase.txt
        echo -e "\nFound:"
        cat optimal_out.txt
        echo -e "\nExpected:"
        cat brute_out.txt
        ok=0
        break
    else
        echo -e "Test case $testcase_number: ${AC_COLOR}ACCEPTED${RESET_COLOR}"
    fi
done

if [ $ok -ne 0 ]
then
  echo -e "\n----------${AC_COLOR}PASSED ALL TESTCASES${RESET_COLOR}-----------"
else
  echo -e "\n----------${WA_COLOR}FAILED SOME TESTCASES${RESET_COLOR}----------"
fi