import os
from recolor import Core

nomes = [
'Normal18.jpg',
'Normal19.jpg',
'Normal20.jpg',
'Normal21.jpg',
'Normal22.jpg',
'Normal23.jpg'
]

def process(filename):

    name, _ = os.path.splitext(filename)  # Separar o nome do arquivo da extensão
    save_filename = f'{name}'

    # Correcting Image for Protanopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_2/{filename}',
                 return_type='save',
                 save_path=f'./imgs/Protanopia/Pag_2/Protanopia_{save_filename}.png',
                 protanopia_degree=1.0,
                 deutranopia_degree=0.0)


    # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_2/{filename}',
                 return_type='save',
                 save_path=f'./imgs/Deuteranopia/Pag_2/Deuteranopia_{save_filename}.png',
                 protanopia_degree=0.0,
                 deutranopia_degree=1.0)


    # Correcting Image for Hybrid with diagnosed degree of 1.0 for both protanopia and
    # deutranopia and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_2/{filename}',
                return_type='save',
                save_path=f'./imgs/Tritanopia/Pag_2/Tritanopia_{save_filename}.png',
                protanopia_degree=1.0,
                deutranopia_degree=1.0)

    # # Simulating Protanopia with diagnosed degree of 0.9 and saving the image to file.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_protanopia.png',
    #               simulate_type='protanopia',
    #               simulate_degree_primary=0.9)

    # # Simulating Deutranopia with diagnosed degree of 0.9 and saving the image to file.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_deutranopia.png',
    #               simulate_type='deutranopia',
    #               simulate_degree_primary=0.9)

    # # Simulating Tritanopia with diagnosed degree of 0.9 and saving the image to file.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_tritanopia.png',
    #               simulate_type='tritanopia',
    #               simulate_degree_primary=0.9)

    # # Simulating Hybrid (Protanomaly + Deutranomaly) with diagnosed degree of 0.9 and 1.0 and saving the image to file.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_hybrid.png',
    #               simulate_type='hybrid',
    #               simulate_degree_primary=0.5,
    #               simulate_degree_sec=0.5)

    # # Also simulate the corrected image to see difference.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_corrected_protanopia.png',
    #               simulate_type='protanopia',
    #               simulate_degree_primary=0.9)
    
    # # Also simulate the corrected image to see difference.
    # Core.simulate(input_path=f'./imgs/Normal/Pag_1/{filename}',
    #               return_type='save',
    #               save_path='Examples_Check/ex_simulate_corrected_deutranopia.png',
    #               simulate_type='deutranopia',
    #               simulate_degree_primary=0.9)
    


    # You can also use different return types and get numpy array or PIL.Image for further processing.
    # See recolor.py
    return

def main():
    for nome in nomes:
        process(nome)

if __name__ == '__main__':
    main()
