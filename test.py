# Tests for format_time()
import dateandtime as cdt
import unittest

# could use many more test cases to be thorough, but this will do for now since 
# I'm having to manually type all of these
class TestFormatTime(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            # invalid current_format
            cdt.format_time("12:34", "hhmm", "seconds")
            cdt.format_time("12:34", "hh:mm:ss", "seconds")
            cdt.format_time("12:34", "seconds", "json")
            cdt.format_time("12:34", "json", "seconds")
            cdt.format_time("12:34", "invalid", "seconds")

            #invalid new_format
            cdt.format_time("12:34", "hh:mm", "invalid")

            #invalid time
            cdt.format_time("25:34", "hh:mm", "seconds")
            cdt.format_time("12:90", "hh:mm", "seconds")
            cdt.format_time("25:90", "hh:mm", "seconds")

    def test_hhmm(self):
        
        self.assertEqual(cdt.format_time("12:34", "hh:mm", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time("09:56", "hh:mm", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time("12:34", "hh:mm", "hhmm"), "1234") # to hhmm
        self.assertEqual(cdt.format_time("09:56", "hh:mm", "hhmm"), "0956")  #to hhmm
        self.assertEqual(cdt.format_time("12:34", "hh:mm", "hh:mm:ss"), "12:34:00") # to hh:mm:ss
        self.assertEqual(cdt.format_time("09:56", "hh:mm", "hh:mm:ss"), "09:56:00")  # to hh:mm:ss
        self.assertEqual(cdt.format_time("12:34", "hh:mm", "seconds"), 45240) # to seconds
        self.assertEqual(cdt.format_time("09:56", "hh:mm", "seconds"), 35760) # to seconds 

    def test_hhcolonmm(self):
        self.assertEqual(cdt.format_time("1234", "hhmm", "json"), "placeholder") # to json 
        self.assertEqual(cdt.format_time("0956", "hhmm", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time("1234", "hhmm", "hh:mm"), "12:34") # to hh:mm
        self.assertEqual(cdt.format_time("0956", "hhmm", "hh:mm"), "09:56") # to hh:mm  
        self.assertEqual(cdt.format_time("1234", "hhmm", "hh:mm:ss"), "12:34:00") # to hh:mm:ss
        self.assertEqual(cdt.format_time("0956", "hhmm", "hh:mm:ss"), "09:56:00") # to hh:mm:ss 
        self.assertEqual(cdt.format_time("1234", "hhmm", "seconds"), 45240) # to seconds
        self.assertEqual(cdt.format_time("0956", "hhmm", "seconds"), 35760) # to seconds

    def test_hhmmss(self):
        self.assertEqual(cdt.format_time("12:34:00", "hh:mm:ss", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time("09:56:00", "hh:mm:ss", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time("12:34:00", "hh:mm:ss", "hhmm"), "1234") # to hhmm
        self.assertEqual(cdt.format_time("09:56:00", "hh:mm:ss", "hhmm"), "0956") # to hhmm 
        self.assertEqual(cdt.format_time("12:34:00", "hh:mm:ss", "hh:mm"), "12:34") # to hh:mm
        self.assertEqual(cdt.format_time("09:56:00", "hh:mm:ss", "hh:mm"), "09:56") # to hh:mm 
        self.assertEqual(cdt.format_time("12:34:00", "hh:mm:ss", "seconds"), 45240) # to seconds
        self.assertEqual(cdt.format_time("09:56:00", "hh:mm:ss", "seconds"), 35760) # to seconds  

    def test_seconds(self):
        self.assertEqual(cdt.format_time(45240, "seconds", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time(35760, "seconds", "json"), "placeholder") # to json
        self.assertEqual(cdt.format_time(45240, "seconds", "hhmm"), "1234") # to hhmm
        self.assertEqual(cdt.format_time(35760, "seconds", "hhmm"), "0956") # to hhmm
        self.assertEqual(cdt.format_time(45240, "seconds", "hh:mm"), "12:34") # to hh:mm
        self.assertEqual(cdt.format_time(35760, "seconds", "hh:mm"), "09:56") # to hh:mm
        self.assertEqual(cdt.format_time(45240, "seconds", "hh:mm:ss"), "12:34:00") # to hh:mm:ss
        self.assertEqual(cdt.format_time(35760, "seconds", "hh:mm:ss"), "09:56:00") # to hh:mm:ss

    def test_json(self):
        # same two examples (12:34, 9:56) in json form
        json1 = {"requested_time": "0","actual_time": "12:34:00","hour": 12,"minute": 34,"second": 0,"message_default": True}        
        json2 = {"requested_time": "0","actual_time": "09:56:00","hour": 9,"minute": 56,"second": 0,"message_default": True}

        self.assertEqual(cdt.format_time(json1, "json", "seconds"), 45240) # to seconds
        self.assertEqual(cdt.format_time(json2, "json", "seconds"), 35760) # to seconds
        self.assertEqual(cdt.format_time(json1, "json", "hhmm"), "1234") # to hhmm
        self.assertEqual(cdt.format_time(json2, "json", "hhmm"), "0956") # to hhmm
        self.assertEqual(cdt.format_time(json1, "json", "hh:mm"), "12:34") # to hh:mm
        self.assertEqual(cdt.format_time(json2, "json", "hh:mm"), "09:56") # to hh:mm
        self.assertEqual(cdt.format_time(json1, "json", "hh:mm:ss"), "12:34:00") # to hh:mm:ss
        self.assertEqual(cdt.format_time(json2, "json", "hh:mm:ss"), "09:56:00") # to hh:mm:ss

    

if __name__ == "__main__":
    unittest.main()




    