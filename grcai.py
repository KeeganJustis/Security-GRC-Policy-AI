from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
import requests
from sans import *


TYPES_OF_POLICIES = {1:{"policy_name":"encryption policy","sans_template": sample_encryption_policy,"cloudsecurity_alliance": cloud_security_alliance_encryption},2:"ACCEPTABLE USE"}

def ask_questions():
    print("Welcome to Guidepoint Policy Engine Creator")
    type_of_policy = choose_type_of_policy(TYPES_OF_POLICIES)
    company_name = choose_company_name()
    employees = select_num_employees()
    industry = select_company_industry()
    cloud_provider = select_cloud_provider()
    pci = is_pci_required()
    hippa = is_hippa_required()
    endpoint = select_endpoint_protection()
    cnap = select_cnap()
    seim = select_seim()
    additional_tools = other_tools()
    print('\n\nPlease wait will report is generating')

    compute_llm(type_of_policy,company_name,employees,industry,cloud_provider,pci,hippa,endpoint,cnap,seim,additional_tools)

def choose_type_of_policy(dic_of_policy):
    policy = input("\nWhat type of policy do you want to create?\n1. Encryption Policy (press 1)\n")
    return dic_of_policy[int(policy)]

def choose_company_name():
    return input("\nWhat is the company name?\n")

def select_num_employees():
    return input("\nHow Many Employees does your company have\n")

def select_company_industry():
    return input("\nWhat Industry or domain does your company reside in\n")

def select_cloud_provider():
    return input("\nWhich Cloud Provider'(s) are you using (AWS,Azure,GCP,Oracle,IBM,on-premise,or any combination)")

def is_pci_required():
    pci = input("\nDoes the company accept credit card information (1 for True or 2 for false)\n")
    if int(pci) == 1:
        return True
    else:
        return False

def is_hippa_required():
    hippa = input("\nDoes your company have Health Care Information (1 for True or 2 for false)\n")
    if int(hippa) == 1:
        return True
    else:
        return False

def select_endpoint_protection():
    return input("\nWhich Endpoint Protection Products are you using (CrowdStrike,SentinelOne,ect)\n")
 
def select_cnap():
    return input("\nWhich Cloud-Native Application Protection Platform (CNAPP)' are you using\n")
 
def select_seim():
    return input("\nWhich Security information and event management (SEIM) are you using\n")

def other_tools():
    return input("\nPlease enter any other relevant security tools not mentioned above that you want in the policy with a description of the scope and the what tool is used for\n")

def complete_report():
    pass

def testing_reports():
    pass
   # 1. check for typos
    # series of unit test

def compute_llm(policy,company_name,employees,industry,cloud_provider,pci,hippa,endpoint,cnap,seim,additional_tools):
    cloud_security_alliance = requests.get(policy['cloudsecurity_alliance'])

    model = ChatOpenAI(model='gpt-4',temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You're a Chief Security Officer for {company_name} and you will be writing an {policy}",
            ),
            (
                "system",
                "an example is is the following {sample_policy}",
            ),
            (
                "system",
                "an second example is is the following {sample_policy_2}",
            ),
            (
                "system",
                "The company run primary on {cloud_provider} and has {employees} employees.",
            ),
            (
                "system",
                "please refered to the cloud security alliance guidelines {cloud_security_alliance} when making the policies"
            ),
            (
                "human",
                "write an encryption policy for an {company_name} in the {industry} field. Included specfic references to {cloud_provider} resources and workstations and the specfic encryption strength used for at rest and in transit "
            ),
        ]
    )
    runnable = prompt | model | StrOutputParser()

    my_policy= runnable.invoke({"policy":policy['policy_name'],"company_name": company_name,"sample_policy":policy['sans_template'],"cloud_provider":cloud_provider,"employees":employees,"company_name":company_name,"industry":industry,"cloud_security_alliance":cloud_security_alliance.text,"sample_policy_2":sample_encryption_policy_2})
                                #'aws_best_practice_data_in_transit_1':aws_best_practice_data_in_transit_1.text,"aws_best_practice_data_in_transit_2":aws_best_practice_data_in_transit_2.text,"aws_best_practice_data_in_transit_3":aws_best_practice_data_in_transit_3.text,"aws_best_practice_data_in_transit_4":aws_best_practice_data_in_transit_4.text})


    print(my_policy)


# abb31e66-b772-46af-be85-163a08587cd3

def main():
    ask_questions()

if __name__ == "__main__":
    main()