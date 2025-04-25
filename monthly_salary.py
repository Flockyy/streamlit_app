import json
import csv
from tabulate import tabulate

def import_data() -> dict:
    """
    Import raw data from a JSON file.

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

def get_stats(affiliate: str = None) -> dict:
    """
    Get statistics for all affiliates or a specific affiliate.

    Args:
        affiliate (str, optional): Affiliate name. Defaults to None.

    Returns:
        dict: statistics including mean, lowest, and highest salary
    """
    
    if affiliate:
        data = get_item_by_affiliate(affiliate)
    else:
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


def show_stats(affiliate: str = None) -> None:
    """
    Show statistics for all affiliates or a specific affiliate.

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


show_stats('TechCorp')
data = prepare_csv()
export_to_csv('./app/data/employes_data_test.csv')
print("Data exported to employes_data_test.csv")
