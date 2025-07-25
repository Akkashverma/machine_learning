from setuptools import  find_packages , setup
from typing import List



hypen_e = '-e.'
def get_req(file_path:str)->list[str]:
    ''' this func will return thr list of requirements'''


    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [r.replace("\n","")for r in requirements]
        
        if hypen_e in requirements:
            requirements.remove(hypen_e)

    return requirements


setup(


name='mlproject',
version = '0.0.1',
author = 'Akash',
author_email= 'akash190427@gmail.com',
packages= find_packages(),
install_requires = get_req('requirements.txt')

)