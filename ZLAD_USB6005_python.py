# Environment:

# Window 10
# USB driver: Microsoft 2006/6/21 10.0.19041.1 

from ctypes import *
import os

from ctypes.wintypes import BOOL, DWORD, HANDLE

# 此处根据电脑配置进行选择 x64 or x86

CUR_PATH=os.path.dirname('x64/')
dllPath=os.path.join(CUR_PATH,"FTAPI.dll")
mydll = windll.LoadLibrary(dllPath)


value_number = c_long(0)
value_get_numberOfDev = mydll.get_numberOfDev(pointer(value_number))

print('This is the number of USB connected', value_number)
print("The bool of value_get_numberOfDev is ",value_get_numberOfDev)


value_handle_one = HANDLE()
value_handle_two = HANDLE()

bool_open_device_one = mydll.open_device(0,pointer(value_handle_one))
bool_open_device_two = mydll.open_device(1,pointer(value_handle_two))

print('This is the handle value of value_open_device_one', value_handle_one)
print('This is the handle value of value_open_device_two', value_handle_two)

print("The bool_open_device_one is ",bool_open_device_one)
print("The bool_open_device_two is ",bool_open_device_two)


# analog_in_all

ch_one = DWORD()
data_range_one = DWORD()
out_value_one = c_double(0)

ch_two = DWORD()
data_range_two = DWORD()
out_value_two = c_double(0)

out_all_value_one = (c_double * 8) ()
out_all_value_two = (c_double * 8) ()

all_data_range_one = DWORD()
all_data_range_two = DWORD()

bool_analog_in_all_one =mydll.analog_in_all(value_handle_one, all_data_range_one, out_all_value_one)
bool_analog_in_all_two =mydll.analog_in_all(value_handle_two, all_data_range_two, out_all_value_two)

print("The bool of value_analog_in_all_one is ",bool_analog_in_all_one)
print("The bool of value_analog_in_all_two is ",bool_analog_in_all_two)

for i in range(8):
    print("The value_analog_in_all_one and its out_value is ", out_all_value_one[i])
    print("The value_analog_in_all_two and its out_value is ", out_all_value_two[i])


# gpio_out_single

# 128 for 1111 1111

# 1,2,4,8,16,32,64,128

ch_gpio_out_single_one = DWORD(128)

ch_gpio_out_single_two = DWORD(128)


value_gpio_out_single_one = DWORD(1)

value_gpio_out_single_two = DWORD(1)

bool_gpio_out_single_one = mydll.gpio_out_all(value_handle_one,ch_gpio_out_single_one,value_gpio_out_single_one)
bool_gpio_out_single_two = mydll.gpio_out_all(value_handle_two,ch_gpio_out_single_two,value_gpio_out_single_two)


print('The bool_gpio_out_single_one is', bool_gpio_out_single_one)
print('The bool_gpio_out_single_two is', bool_gpio_out_single_two)


# gpio_out_status

value_data_one = DWORD()
value_data_two = DWORD()

grip_out_value_one = (c_int * 8) ()
grip_out_value_two = (c_int * 8) ()

bool_gpio_out_status_one = mydll.gpio_out_status(value_handle_one,value_data_one,pointer(grip_out_value_one))
bool_gpio_out_status_two = mydll.gpio_out_status(value_handle_two,value_data_two,pointer(grip_out_value_two))

print("The bool_gpio_out_status_one is ",bool_gpio_out_status_one)
print("The bool_gpio_out_status_two is ",bool_gpio_out_status_two)

for i in range(8):

    print("The value_gpio_out_status_one and its out_value is ", grip_out_value_one[i])
    print("The value_gpio_out_status_two and its out_value is ", grip_out_value_two[i])

# gpio_in_all

value_data_one = DWORD()
value_data_two = DWORD()

grip_in_value_one = (c_int * 8) ()
grip_in_value_two = (c_int * 8) ()

bool_gpio_in_all_one = mydll.gpio_in_all(value_handle_one,value_data_one,pointer(grip_in_value_one))
bool_gpio_in_all_two = mydll.gpio_in_all(value_handle_two,value_data_two,pointer(grip_in_value_two))

print("The bool_gpio_in_all_one is ",bool_gpio_in_all_one)
print("The bool_gpio_in_all_two is ",bool_gpio_in_all_two)

for i in range(8):

    print("The value_gpio_in_all_one and its out_value is ", grip_in_value_one[i])
    print("The value_gpio_in_all_two and its out_value is ", grip_in_value_two[i])

# close_device

if value_handle_one !=0:

    bool_close_device_one = mydll.close_device(value_handle_one)
    print('This is the value of value_handle', value_handle_one)
    print("The bool_close_device_one is ",bool_close_device_one)

if value_handle_two !=0:

    bool_close_device_two = mydll.close_device(value_handle_two)
    print('This is the value of value_handle', value_handle_two)
    print("The bool_close_device_two is ",bool_close_device_two)










