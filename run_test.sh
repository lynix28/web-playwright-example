#!/bin/bash
source test_list.sh
ENV_FILE=".env"
BROWSER="chromium"  # Set the default browser value here
HEADLESS="false"  # Set the default headless value here

run_registered_test() {
    pytest "$1"
}

update_env_variable() {
    awk -v key="$1" -v value="$2" 'BEGIN{FS=OFS="="} $1==key{$2=value} 1' "$ENV_FILE" > "$ENV_FILE.tmp" && mv "$ENV_FILE.tmp" "$ENV_FILE"
}

display_help() {
    echo "Usage: ./run_test.sh [test_case] [--browser browser_name] [--headless true/false]"
    echo
    echo "Examples:"
    echo "  ./run_test.sh"
    echo "  ./run_test.sh login"
    echo "  ./run_test.sh login --browser firefox"
    echo "  ./run_test.sh login --browser chromium --headless true"
    echo
    echo "Browser Support:"
    echo "  chromium | firefox | webkit"
}

if [[ $# -eq 0 ]]; then
    update_env_variable "BROWSER" "$BROWSER"
    update_env_variable "HEADLESS" "$HEADLESS"
    pytest ./tests/*
elif [[ $1 == "--help" ]]; then
    display_help
    exit 0
elif [[ $# -gt 0 && $# -lt 5 ]]; then
    if [[ $# -eq 4 ]]; then
        if [[ $1 == "--headless" && $3 == "--browser" ]]; then
            update_env_variable "HEADLESS" "$2"
            update_env_variable "BROWSER" "$4"
        elif [[ $1 == "--browser" && $3 == "--headless" ]]; then
            update_env_variable "BROWSER" "$2"
            update_env_variable "HEADLESS" "$4"
        fi
        pytest ./tests/*
    elif [[ $1 == "--headless" || $1 == "--browser" ]]; then
        if [[ -n $2 ]]; then
            variable=$1
            if [[ $1 == "--headless" ]]; then
                update_env_variable "BROWSER" "$BROWSER"
                update_env_variable "HEADLESS" "$2"
            elif [[ $1 == "--browser" ]]; then
                update_env_variable "HEADLESS" "$HEADLESS"
                update_env_variable "BROWSER" "$2"
            fi
            pytest ./tests/*
        else
            echo "Invalid arguments. Check './run_test.sh --help'"
            exit 1
        fi
    else
        if [[ -z $2 ]]; then
            update_env_variable "BROWSER" "$BROWSER"
            update_env_variable "HEADLESS" "$HEADLESS"
            test_case=$1
            if declare -p "$test_case"_tests &>/dev/null; then
                test_files="${test_case}_tests[@]"
                for test_file in "${!test_files}"; do
                    run_registered_test "$test_file"
                done
            else
                echo "Invalid test case. Please provide a valid test case name."
                exit 1
            fi
        elif [[ $2 == "--headless" || $2 == "--browser" ]]; then
            if [[ $2 == "--browser" ]]; then
                update_env_variable "BROWSER" "$3"
                update_env_variable "HEADLESS" "$HEADLESS"
            elif [[ $2 == "--headless" ]]; then
                update_env_variable "HEADLESS" "$3"
                update_env_variable "BROWSER" "$BROWSER"
            else
                echo "Invalid arguments. Check './run_test.sh --help'"
                exit 1
            fi
            test_case=$1
            if declare -p "$test_case"_tests &>/dev/null; then
                test_files="${test_case}_tests[@]"
                for test_file in "${!test_files}"; do
                    run_registered_test "$test_file"
                done
            else
                echo "Invalid test case. Please provide a valid test case name."
                exit 1
            fi
        else
            echo "Invalid arguments. Check './run_test.sh --help'"
            exit 1
        fi
    fi
elif [[ $# -gt 2 && $# -lt 6 ]]; then
    if [[ $# -eq 5 ]]; then
        if [[ $2 == "--headless" && $4 == "--browser" ]]; then
            update_env_variable "HEADLESS" "$3"
            update_env_variable "BROWSER" "$5"
        elif [[ $2 == "--browser" && $4 == "--headless" ]]; then
            update_env_variable "BROWSER" "$3"
            update_env_variable "HEADLESS" "$5"
        fi
        test_case=$1
        if declare -p "$test_case"_tests &>/dev/null; then
            test_files="${test_case}_tests[@]"
            for test_file in "${!test_files}"; do
                run_registered_test "$test_file"
            done
        else
            echo "Invalid test case. Please provide a valid test case name."
            exit 1
        fi
    else
        if [[ $2 == "--browser" ]]; then
            update_env_variable "BROWSER" "$3"
            update_env_variable "HEADLESS" "$HEADLESS"
        elif [[ $2 == "--headless" ]]; then
            update_env_variable "HEADLESS" "$3"
            update_env_variable "BROWSER" "$BROWSER"
        else
            echo "Invalid arguments. Check './run_test.sh --help'"
            exit 1
        fi
        test_case=$1
        if declare -p "$test_case"_tests &>/dev/null; then
            test_files="${test_case}_tests[@]"
            for test_file in "${!test_files}"; do
                run_registered_test "$test_file"
            done
        else
            echo "Invalid test case. Please provide a valid test case name."
            exit 1
        fi
    fi
else
    echo "Invalid arguments. Check './run_test.sh --help'"
    exit 1
fi