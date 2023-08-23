from UI.parsers import *
import Models.test as test

opt_settings = {"model":{"parser":parse_model, 
                         "args":[["test", "test2", "test3", "test4", "test5", "test6", "test7", "drone", 
                                  "consensus", "hol", "robot"]], 
                         "flags":["--model"],
                         "default":test.get_model_2()
                         },
                "num_samples":{
                    "parser":parse_num, 
                    "args":[int,1], 
                    "flags":["-N"],
                    "default":100
                    },
                "batch_size":{
                    "parser":parse_num,
                    "args":[int,1],
                    "flags":["--batch"],
                    "default":150
                    },
                "beta":{
                    "parser":parse_num,
                    "args":[float,0,1], 
                    "flags":["-beta"],
                    "default":1e-5
                    },
                "lambda":{
                    "parser":parse_num,
                    "args":[float, 0, 1], 
                    "flags":["-lambda"],
                    "default":None
                    },
                "rho":{
                    "parser":parse_num,
                    "args":[float,0], 
                    "flags":["-rho"],
                    "default":1
                    },
                "MC":{
                    "parser":parse_bool,
                    "args":[], 
                    "flags":["--MC"],
                    "default":False
                    },
                "MC_samples":{
                    "parser":parse_num,
                    "args":[int, 1], 
                    "flags":["--MC_samples"],
                    "default":10000
                    },
                "debug_level":{
                    "parser":parse_debug,
                    "args":[],
                    "flags":["-v","-d", "-vo", "-do"],
                    "default":None
                    },
                "tol":{
                    "parser":parse_num,
                    "args":[float, 0, 1],
                    "flags":["--tol"],
                    "default":1e-5
                    },
                "sample_load_file":{
                        "parser":parse_file,
                        "args":[True],
                        "flags":["--load"],
                        "default":None
                        },
                "sample_save_file":{
                        "parser":parse_file,
                        "args":[False],
                        "flags":["--save"],
                        "default":None
                        },
                "result_save_file":{
                        "parser":parse_file,
                        "args":[False],
                        "flags":["--save_res"],
                        "default":None
                        },
                "prob_load_file":{
                        "parser":parse_file,
                        "args":[True],
                        "flags":["--load_res"],
                        "default":None
                        },
                "test_supps":{
                        "parser":parse_bool,
                        "args":[],
                        "flags":["--test_support"],
                        "default":False
                        },
                "sg_itts":{
                        "parser":parse_num,
                        "args":[int, 1],
                        "flags":["--sg_itt"],
                        "default":500
                        },
                "FSP_itts":{
                        "parser":parse_num,
                        "args":[int, 1],
                        "flags":["--sg_itt"],
                        "default":10000
                        },
                "file_write":{
                        "parser":parse_bool,
                        "args":[],
                        "flags":["--file_out"],
                        "default":False,
                        },
                }

inst_opts = {"brp":["256,15","4096,5"],
             "consensus": ["2,2","2,32","4,2","4,4"],
             "sav": ["6,2,2", "100,10,10", "6,2,2", "10,3,3"],
             "zeroconf": ["2", "5"]
             }
