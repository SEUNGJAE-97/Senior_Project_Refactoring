import KerasData as KerasData

class KerasMain():
    def __init__(self):
        Model_info = {
            'Class_Num'     :   4,
            'Batch_Size'    :   16,
            'Input_Dim'     :   200,
            'Learning_Rate' :   0.004,
            'Epochs'        :   10,
            'Model_Name'    :   'Alyak',
            'Data_Path'     :   'D:/image_set',
            'Save_Path'     :   'D:/'
        }

        self.m_KerasData = KerasData.KerasData()

    def main(self):
        print("\n[ Data ]\n")
        self.m_KerasData.Collect_Image()

if __name__ == '__main__':
    Main_Class = KerasMain()
    Main_Class.main()
