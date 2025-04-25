import json
import csv
from tabulate import tabulate

def import_data() -> dict:
    """
    Import raw data from a JSON file.
    This function reads a JSON file containing employee data and returns the data as a dictionary.
    The JSON file is expected to be in the following format:
    {
        "affiliate1": [
            {
                "name": "John Doe",
                "weekly_hours_worked": 40,
                "contract_hours": 35,
                "hourly_rate": 20
            },
            ...
        ],
        "affiliate2": [
            ...
        ]
    }
    

    Args:
        None

    Returns:
        dict: returns the data from the JSON file.
    """
    with open('/Users/fabgrall/Documents/data_engineer/monthly_salary/employes_data_test.json') as f:
        data = json.load(f)
        
    return data

def get_all_items() -> list:
    """
    Get all items from the JSON file and pre-compute their monthly salary.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the keys 'weekly_hours_worked', 'contract_hours', and 'hourly_rate'.
    The function calculates the weekly salary based on the hours worked and the contract hours,
    and then computes the monthly salary by multiplying the weekly salary by 4.
    If the employee worked more hours than their contract hours, the extra hours are paid at 1.5 times the hourly rate.
    The function adds the 'week_salary' and 'monthly_salary' keys to each employee's dictionary.
    The function returns the modified data with the added keys.
    This function reads a JSON file containing employee data and returns the data as a list.

    Args:
        None
    
    Returns:
        list: list of all employees with their monthly salary.
    """
    with open('/Users/fabgrall/Documents/data_engineer/monthly_salary/employes_data_test.json') as f:
        data = json.load(f)
    all_data = []

    for x in data:
        for y in data[x]:
            all_data.append(y)
            
    all_data = compute_monthly_salary(all_data)
    
    return all_data


def get_item_by_affiliate(affiliate: str) -> list:
    """
    Get items by affiliate from the JSON file and pre-compute their monthly salary.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the keys 'weekly_hours_worked', 'contract_hours', and 'hourly_rate'.
    The function calculates the weekly salary based on the hours worked and the contract hours,
    and then computes the monthly salary by multiplying the weekly salary by 4.
    If the employee worked more hours than their contract hours, the extra hours are paid at 1.5 times the hourly rate.
    The function adds the 'week_salary' and 'monthly_salary' keys to each employee's dictionary.
    The function returns the modified data with the added keys.

    Args:
        affiliate (str): Affiliate name

    Returns:
        list: List of employees from the affiliate
    """
    with open('/Users/fabgrall/Documents/data_engineer/monthly_salary/employes_data_test.json') as f:
        data = json.load(f)

    data = data[affiliate]
    data = compute_monthly_salary(data)
    return data


def compute_monthly_salary(data: list) -> list:
    """
    Compute the monthly salary for each employee in the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the keys 'weekly_hours_worked', 'contract_hours', and 'hourly_rate'.
    The function calculates the weekly salary based on the hours worked and the contract hours,
    and then computes the monthly salary by multiplying the weekly salary by 4.
    If the employee worked more hours than their contract hours, the extra hours are paid at 1.5 times the hourly rate.
    The function adds the 'week_salary' and 'monthly_salary' keys to each employee's dictionary.
    The function returns the modified data with the added keys.

    Args:
        data (list): List of employees

    Returns:
        dict: list of employees with their monthly salary
    """
    
    for i in data:
        if i['weekly_hours_worked'] > i['contract_hours']:
            i['week_salary'] = i['contract_hours'] * i['hourly_rate'] + \
                (i['weekly_hours_worked'] - i['contract_hours']) * i['hourly_rate'] * 1.5
            i['monthly_salary'] = i['week_salary'] * 4
        else:
            i['week_salary'] = i['weekly_hours_worked'] * i['hourly_rate']
            i['monthly_salary'] = i['week_salary'] * 4
            
    return data


def mean_salary(data: list) -> float:
    """
    Compute the mean salary from the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the mean salary by summing all the monthly salaries
    and dividing by the number of employees.
    The function returns the mean salary as a float.

    Args:
        data (_type_): List of employees

    Returns:
        float: mean salary
    """

    data_length = len(data)
    mean_sal = 0

    for i in data:
        mean_sal += i['monthly_salary']
        
    mean_sal = mean_sal / data_length
    
    return mean_sal


def lowest_salary(data: list) -> float:
    """
    Compute the lowest salary from the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the lowest salary by iterating through the data
    and comparing each employee's monthly salary to the current lowest salary.
    The function returns the lowest salary as a float.

    Args:
        data (list): list of employees

    Returns:
        float: lowest salary
    """
    mean_sal = mean_salary(data)
    lowest_sal = mean_sal

    for i in data:
        if i['monthly_salary'] < lowest_sal:
            lowest_sal = i['monthly_salary']
            
    return lowest_sal


def highest_salary(data: list) -> float:
    """
    Compute the highest salary from the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the highest salary by iterating through the data
    and comparing each employee's monthly salary to the current highest salary.
    The function returns the highest salary as a float.
    

    Args:
        data (list): list of employees

    Returns:
        float: highest salary
    """
    
    mean_sal = mean_salary(data)
    highest_sal = mean_sal

    for i in data:
        if i['monthly_salary'] > highest_sal:
            highest_sal = i['monthly_salary']
            
    return highest_sal


def get_global_stats() -> dict:
    """
    Get global statistics from the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the mean, lowest, and highest salary by calling
    the respective functions and returns them in a dictionary.
    Args:
        None
    Returns:
        dict: global statistics including mean, lowest, and highest salary
    """
    
    data = get_all_items()
    mean_sal = mean_salary(data)
    lowest_sal = lowest_salary(data)
    highest_sal = highest_salary(data)
    
    return {
        'mean_salary': mean_sal,
        'lowest_salary': lowest_sal,
        'highest_salary': highest_sal
    }


def get_stats_by_affiliate(affiliate: str) -> dict:
    """
    Get statistics by affiliate from the data.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the mean, lowest, and highest salary by calling
    the respective functions and returns them in a dictionary.

    Args:
        affiliate (str): affiliate name

    Returns:
        dict: statistics for the affiliate including mean, lowest, and highest salary
    """
    
    data = get_item_by_affiliate(affiliate)
    mean_sal = mean_salary(data)
    lowest_sal = lowest_salary(data)
    highest_sal = highest_salary(data)
    
    return {
        'mean_salary': mean_sal,
        'lowest_salary': lowest_sal,
        'highest_salary': highest_sal
    }


def show_stats(affiliate=None) -> None:
    """
    Show statistics for all affiliates or a specific affiliate.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the key 'monthly_salary'.
    The function calculates the mean, lowest, and highest salary by calling
    the respective functions and prints them in a formatted table.
    If an affiliate is provided, it shows the statistics for that affiliate.
    If no affiliate is provided, it shows the statistics for all affiliates.
    The function returns None. 

    Args:
        affiliate (str, optional): Affiliate None. Defaults to None.
    
    Returns:
        None
    """
    
    if affiliate:
        stats = get_stats_by_affiliate(affiliate)
        print(f"Statistics for {affiliate}:")
        data = get_item_by_affiliate(affiliate)
        data = sorted(data, key=lambda x: x['monthly_salary'], reverse=True)
        print(tabulate(data, headers="keys", tablefmt="grid"))  
        print(f"Mean Salary: {stats['mean_salary']}")
        print(f"Lowest Salary: {stats['lowest_salary']}")
        print(f"Highest Salary: {stats['highest_salary']}")
    else:
        stats = get_global_stats()
        print(f"Statistics for all affiliates:")
        data = get_all_items()
        data = sorted(data, key=lambda x: x['monthly_salary'], reverse=True)
        print(tabulate(data, headers="keys", tablefmt="grid"))
        print(f"Mean Salary: {stats['mean_salary']}")
        print(f"Lowest Salary: {stats['lowest_salary']}")
        print(f"Highest Salary: {stats['highest_salary']}")
        
    return

def prepare_csv() -> dict:
    """
    Prepare data for CSV export.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the keys 'weekly_hours_worked', 'contract_hours', and 'hourly_rate'.
    The function calculates the weekly salary based on the hours worked and the contract hours,
    and then computes the monthly salary by multiplying the weekly salary by 4.
    If the employee worked more hours than their contract hours, the extra hours are paid at 1.5 times the hourly rate.
    The function adds the 'week_salary' and 'monthly_salary' keys to each employee's dictionary.
    The function sorts the data by monthly salary in descending order and adds the mean, lowest, and highest salary
    to the first employee's dictionary.
    The function returns the modified data as a dictionary.
    Args:
        None

    Returns:
        dict: list of employees with their monthly salary
    """
    data = import_data()
    for key, value in data.items():
        for i in value:
            if i['weekly_hours_worked'] > i['contract_hours']:
                i['week_salary'] = i['contract_hours'] * i['hourly_rate'] + \
                    (i['weekly_hours_worked'] - i['contract_hours']) * i['hourly_rate'] * 1.5
                i['monthly_salary'] = i['week_salary'] * 4
            else:
                i['week_salary'] = i['weekly_hours_worked'] * i['hourly_rate']
                i['monthly_salary'] = i['week_salary'] * 4
    
    for i in data:
        data[i] = sorted(data[i], key=lambda x: x['monthly_salary'], reverse=True)
        data[i][0]['mean_salary'] = mean_salary(data[i])
        data[i][0]['lowest_salary'] = lowest_salary(data[i])
        data[i][0]['highest_salary'] = highest_salary(data[i])

    return data


def export_to_csv(filename: str) -> None:
    """
    Export data to a CSV file.
    This function assumes that the data is a list of dictionaries, where each dictionary
    represents an employee with the keys 'weekly_hours_worked', 'contract_hours', and 'hourly_rate'.
    The function calculates the weekly salary based on the hours worked and the contract hours,
    and then computes the monthly salary by multiplying the weekly salary by 4.
    If the employee worked more hours than their contract hours, the extra hours are paid at 1.5 times the hourly rate.
    The function adds the 'week_salary' and 'monthly_salary' keys to each employee's dictionary.
    The function sorts the data by monthly salary in descending order and adds the mean, lowest, and highest salary
    to the first employee's dictionary.
    The function writes the data to a CSV file with the specified filename.
    The CSV file will have the following columns: 'affiliate', 'name', 'weekly_hours_worked', 'contract_hours', 'hourly_rate', 'week_salary', 'monthly_salary', 'job', 'highest_salary', 'mean_salary', and 'lowest_salary'.
    The function returns None.

    Args:
        filename (str): Name of the CSV file to export the data to.
    
    Returns:
        None
        
    """
    data = prepare_csv()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['affiliate', 'name', 'weekly_hours_worked', 'contract_hours', 'hourly_rate', 'week_salary', 'monthly_salary', 'job', 'highest_salary', 'mean_salary', 'lowest_salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for affiliate, employees in data.items():
            for employee in employees:
                employee['affiliate'] = affiliate
                writer.writerow(employee)
    return


show_stats()
data = prepare_csv()
export_to_csv('./app/data/employes_data_test.csv')
print("Data exported to employes_data_test.csv")
