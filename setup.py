#This file is responsible for creating my ML project as a package
from setuptools import setup,find_packages
# find_packages --> it is responsible for all the packages in directory we a re creating
from typing import List # it is used whisc type of vslues your functionn will return

Hyphen_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]: # it will take file path as a parameter and return list of strings
    requirements=[]
    with open(file_path) as file: #openig the passed file
        requirements=file.readlines() # line by line reading of file with \n
        requirements=[req.replace("\n","") for req in requirements] # it will remove all \n 
        #when requirenments.txt file is read , -e . is also in requirements list. We have to remove it 
        if Hyphen_E_dot in requirements:
            requirements.remove(Hyphen_E_dot)
    return requirements


#Following is the meta data of our project
setup(
    name = 'mlproject',
    version='0.0.1',
    author = 'Amna Ali',
    packages= find_packages(),
    #install_requires=['numpy','pandas','seaborn','matplotlib'] # all the requirements for this project.
    # AS there are a lot of requirements so instead of creating the list we will create a funcyion.
    install_requires = get_requirements('requirements.txt')
)

# kon si file ko ye package consider kre ga .. us k lye hmein aik aur folder bnana ho ga us mein __init__.py name ki file bnayein 
# aur jis jis folder mein ye file ho gy us ko as a package consider kya jaye aur us ko import kr skty hain saare project development 
# us naye folder mein ho gy.

#jb bhi hmm requirements ko install krein gy to hmary setup,py ki file lazmi run ho gy is chhez ko enable krne k lye 
#-e . likhein gy requirement.py k function mein

# ye sb krne k baad terminal prr command chlani hai 
#pip install -r requirements.txt
# ==ye sb packages ko install kr de gy aur aik nya folder mlproject.egg-info ka bnn jaye ga
