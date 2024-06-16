import os
from recolor import Core

nomes = [
'Normal1.jpg',
'Normal10.jpg',
'Normal11.jpg',
'Normal12.jpg',
'Normal13.jpg',
'Normal14.jpg',
'Normal15.jpg',
'Normal16.jpg',
'Normal17.jpg',
'Normal1_2.jpg',
'Normal1_2_3.jpg',
'Normal2.jpg',
'Normal3.jpg',
'Normal4.jpg',
'Normal5.jpg',
'Normal6.jpg',
'Normal7.jpg',
'Normal8.jpg',
'Normal9.jpg',
'Normal_Menu.jpg',
]

def process(filename):
        
    name, _ = os.path.splitext(filename)  # Separar o nome do arquivo da extensão
    save_filename = f'{name}'

    # Correcting Image for Protanopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_1/{filename}',
                 return_type='save',
                 save_path=f'./imgs/Protanopia/Pag_1/Protanopia_{save_filename}.png',
                 protanopia_degree=1.0,
                 deutranopia_degree=0.0)


    # Correcting Image for Deutranopia with diagnosed degree of 1.0 and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_1/{filename}',
                 return_type='save',
                 save_path=f'./imgs/Deuteranopia/Pag_1/Deutranopia_{save_filename}.png',
                 protanopia_degree=0.0,
                 deutranopia_degree=1.0)


    # Correcting Image for Hybrid with diagnosed degree of 1.0 for both protanopia and
    # deutranopia and saving the image to file.
    Core.correct(input_path=f'./imgs/Normal/Pag_1/{filename}',
                return_type='save',
                save_path=f'./imgs/Tritanopia/Pag_1/Tritanopia_{save_filename}.png',
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
