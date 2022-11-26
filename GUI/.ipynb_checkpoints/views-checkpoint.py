import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from input_search_algorithm import Optimize

class App(tk.Tk):
    search_space = [(0.0, 82.99989318847656), 
                    (0.0, 22607.90234375), 
                    (0.0, 755.8787231445312), 
                    (0.0, 24.98193359375), 
                    (-0.00830078125, 84.9219741821289), 
                    (-0.0166015625, 84.89873504638672), 
                    (0.0, 20.802440643310547), 
                    (-0.0007421874906867, 0.9607030749320984), 
                    (0.0, 37.24669647216797), 
                    (50, 90)
                ]
              
    def __init__(self, model):
        super().__init__()

        self.geometry("900x530+100+50")
        self.title("Optimizer")
        self.setFrames()
        self.setUpInput()
        self.setUpOutput()
        self.model = model

    def setFrames(self):
        self.input_frame = tk.Frame(self, width=900, height=140, relief=tk.SOLID, bd=1)
        self.output_frame = tk.Frame(self, width=900, height=140, bg="grey")

        self.input_frame.pack(side=tk.TOP, expand=False, fill=tk.BOTH, padx = 20, pady=(20, 1))
        self.output_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH, padx = 20, pady=(2, 20))
        #self.input_frame.grid_propagate(False)
        self.output_frame.grid_propagate(False)

    def setUpInput(self):
        #############################################################
        ### Rows in the input frame
        self.row1 = tk.Frame(self.input_frame, width=900, height=140)   
        self.row2 = tk.Frame(self.input_frame, width=900, height=140)
        self.row3 = tk.Frame(self.input_frame, width=900, height=140)
        self.row1.grid(column = 0, row = 0, padx = 35, pady= 2)
        self.row2.grid(column = 0, row= 1, padx = 35, pady= 2)
        self.row3.grid(column = 0, row= 2, padx = 35, pady= 2)
        ##############################################################

        ##############################################################
        # Row 1 Elements 
        lng_frame = tk.LabelFrame(self.row1, text = "LNG Flow", width = 100, height= 50)
        self.lng = tk.DoubleVar()
        lng_Entry = tk.Entry(lng_frame, textvariable=self.lng, width = 50)
        lng_Entry.pack()
        lng_frame.pack_propagate(False)
        lng_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        mr_return_temp_frame = tk.LabelFrame(self.row1, text = "MR Return Temperature", width = 100, height= 50)
        self.mr_return_temp = tk.DoubleVar()
        mr_return_temp_Entry = tk.Entry(mr_return_temp_frame, textvariable=self.mr_return_temp, width = 50)
        mr_return_temp_Entry.pack()
        mr_return_temp_frame.pack_propagate(False)
        mr_return_temp_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)
        
        IGV_frame = tk.LabelFrame(self.row1, text = "MR IGV Position", width = 100, height= 50)
        self.IGV = tk.DoubleVar()
        IGV_Entry = tk.Entry(IGV_frame, textvariable=self.IGV, width = 50)
        IGV_Entry.pack()
        IGV_frame.pack_propagate(False)
        IGV_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        HMR_flow_frame = tk.LabelFrame(self.row1, text = "HMR Flow", width = 100, height= 50)
        self.HMR_flow = tk.DoubleVar()
        HMR_flow_Entry = tk.Entry(HMR_flow_frame, textvariable=self.HMR_flow, width = 50)
        HMR_flow_Entry.pack()
        HMR_flow_frame.pack_propagate(False)
        HMR_flow_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)
        
        HR_MR_Ratio_frame = tk.LabelFrame(self.row1, text = "HR/MR Ratio", width = 100, height= 50)
        self.HR_MR_Ratio = tk.DoubleVar()
        HR_MR_Ratio_Entry = tk.Entry(HR_MR_Ratio_frame, textvariable=self.HR_MR_Ratio, width = 50)
        HR_MR_Ratio_Entry.pack()
        HR_MR_Ratio_frame.pack_propagate(False)
        HR_MR_Ratio_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        pNitrogen_frame = tk.LabelFrame(self.row1, text = "% Nitrogen in MR", width = 110, height= 50)
        self.pNitrogen = tk.DoubleVar()
        pNitrogen_Entry = tk.Entry(pNitrogen_frame, textvariable=self.pNitrogen, width = 50)
        pNitrogen_Entry.pack()
        pNitrogen_frame.pack_propagate(False)
        pNitrogen_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)
        
        pMethane_frame = tk.LabelFrame(self.row1, text = "% Methane in MR", width = 110, height= 50)
        self.pMethane = tk.DoubleVar()
        pMethane_Entry = tk.Entry(pMethane_frame, textvariable=self.pMethane, width = 50)
        pMethane_Entry.pack()
        pMethane_frame.pack_propagate(False)
        pMethane_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        #
        # Row 2 Elements
        pEthane_frame = tk.LabelFrame(self.row2, text = "% Ethane in MR", width = 110, height= 50)
        self.pEthane = tk.DoubleVar()
        pEthane_Entry = tk.Entry(pEthane_frame, textvariable=self.pEthane, width = 50)
        pEthane_Entry.pack()
        pEthane_frame.pack_propagate(False)
        pEthane_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        pPropane_frame = tk.LabelFrame(self.row2, text = "% Propane in MR", width = 110, height= 50)
        self.pPropane = tk.DoubleVar()
        pPropane_Entry = tk.Entry(pPropane_frame, textvariable=self.pPropane, width = 50)
        pPropane_Entry.pack()
        pPropane_frame.pack_propagate(False)
        pPropane_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        pButane_frame = tk.LabelFrame(self.row2, text = "% Butane in MR", width = 110, height= 50)
        self.pButane = tk.DoubleVar()
        pButane_Entry = tk.Entry(pButane_frame, textvariable=self.pButane, width = 50)
        pButane_Entry.pack()
        pButane_frame.pack_propagate(False)
        pButane_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        ambient_cond_frame = tk.LabelFrame(self.row2, text = "Ambient Condition", width = 110, height= 50)
        self.ambient_cond = tk.DoubleVar()
        ambient_cond_Entry = tk.Entry(ambient_cond_frame, textvariable=self.ambient_cond, width = 50)
        ambient_cond_Entry.pack()
        ambient_cond_frame.pack_propagate(False)
        ambient_cond_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        kettle_level_frame = tk.LabelFrame(self.row2, text = "LP Propane/MR Kettle Level", width = 160, height= 50)
        self.kettle_level = tk.DoubleVar()
        kettle_level_Entry = tk.Entry(kettle_level_frame, textvariable=self.kettle_level, width = 50)
        kettle_level_Entry.pack()
        kettle_level_frame.pack_propagate(False)
        kettle_level_frame.pack(side=tk.LEFT, pady= (5, 5), padx=(3, 3),  anchor=tk.NW)

        #
        # Row 3

        filedg_button = tk.Button(self.row3, text="load file: ", command=self.loadfile)
        filedg_button.pack(side= tk.LEFT, padx = 10)

        self.filepath = tk.StringVar()
        filepath_entry = tk.Entry(self.row3, textvariable=self.filepath, width= 70, relief=tk.FLAT)
        filepath_entry.pack(side=tk.LEFT, padx = 10)

        self.next_button = tk.Button(self.row3, text = "Next Input", bg = "yellow", state = "disabled", command=self.load_to_input)
        self.next_button.pack(side=tk.LEFT, padx = 20)
        
    def loadfile(self):
        filepath = filedialog.askopenfilename()
        self.filepath.set(filepath)
        try:
            with open(self.filepath.get(), "r") as obj:
                file = obj.readlines()
        except FileNotFoundError as e:
            messagebox.showerror("Error!", "File not found or invalid file path")
            return
        else:
            self.next_button.config(state = "normal")
            self.counter = 0
            self.processed = []
            self.n = len(file)
            for line in file[1:]:
                line = line.replace("\n","")
                line = line.split(",")
                new_line = [float(value) for value in line]
                self.processed.append(new_line)
            print("load complete")
        
    def load_to_input(self):
        if self.counter < 0 or self.counter >= (self.n - 1):
            return
        values = self.processed[self.counter]
        self.lng.set(values[0])
        self.mr_return_temp.set(values[1])
        self.IGV.set(values[2])
        self.HMR_flow.set(values[3])
        self.HR_MR_Ratio.set(values[4])
        self.pNitrogen.set(values[5])
        self.pMethane.set(values[6])
        self.pEthane.set(values[7])
        self.pPropane.set(values[8])
        self.pButane.set(values[9])
        self.ambient_cond.set(values[10])
        self.kettle_level.set(values[11])
        print(values)
        self.counter += 1

    def setUpOutput(self):
        #############################################################
        ### Cols in the input frame
        self.col1 = tk.Frame(self.output_frame, width=400, height=300)   
        self.col2 = tk.Frame(self.output_frame, width=400, height=300, bg = 'grey')

        self.col1.pack_propagate(False)
        self.col2.pack_propagate(False)

        self.col1.grid(column = 0, row = 0, padx = (20, 5), pady= 8)
        self.col2.grid(column = 1, row= 0, padx = 10, pady= 8)
        ##############################################################
        #
        # Column 1 - Text
        self.display = tk.Text(self.col1, height = 140, width=380)
        self.display.pack()

        #
        # Column 2
        self.optimize_but = tk.Button(self.col2, text = "Optimize", fg = "white", bg = "green", width = 15, relief=tk.FLAT, command=self.optimize)
        self.clear_button = tk.Button(self.col2, text = "Clear", fg = "white", bg = "Red", width = 15, relief=tk.FLAT)

        self.optimize_but.pack(pady = (80, 10))
        self.clear_button.pack()

    def optimize(self):
        try:
            lng_flow = self.lng.get()
            mr_return_temp = self.mr_return_temp.get()
            igv = self.IGV.get()
            hmr_flow = self.HMR_flow.get()
            hr_mr_ratio = self.HR_MR_Ratio.get()
            pN = self.pNitrogen.get()
            pM = self.pMethane.get()
            pE = self.pEthane.get()
            pP = self.pPropane.get()
            pB = self.pButane.get()
            ambient_cond = self.ambient_cond.get()
            kettle_level = self.kettle_level.get()

            input = [igv, hmr_flow, hr_mr_ratio, pN, pM, pE, pP, pB, ambient_cond, kettle_level]
            output = np.array([[lng_flow, mr_return_temp]])

            p = Optimize(self.model.predict, input, App.search_space, output)
            text = "---------------------\noptimizing\n"
            self.display.insert('end', text)
            result = p.maximize()
            optimized_input, approximate_output, iterations = result

            text = "Done!\n--------------------------\nOutput:\n\nNumber of iteration: "
            text += str(iterations) + "\n\nOptimized Input:\n"
            for output in optimized_input:
                text += str(output) + "\n"
            

            def percentage_increase(new, old):
                return ((new - old)/new) * 100

            increase = percentage_increase(approximate_output, output)
            text += f"Aproximate LNG Flow: {approximate_output[0, 0]} ({increase[0, 0]}%+)\n "
            text += f"Aproximate LNG Rundown Temperature: {approximate_output[0, 1]} ({increase[0, 1]}%+)\n"

            self.display.insert("end", text)
        except:
            messagebox.showerror("Oops!!", "Something went wrong. \nCheck your Inputs")



        



        


