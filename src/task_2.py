"""
Учитывая следующее шестнадцатеричное представление двоичных данных,
разберите как можно больше информации
"""


data = (
    "021500000000000039b00e0066005748a3111f67121a1818141212141616151616191818"
    "bb100000"
)

binary_data = bin(int(data, 16))[2:]

header_version_msb = int(binary_data[0:8], 2)
header_version_lsb = int(binary_data[8:16], 2)
status_code_msb = int(binary_data[16:24], 2)
status_code_lsb = int(binary_data[24:32], 2)

sensor_start = bool(status_code_msb & 0b00000001)
watchdog = bool(status_code_msb & 0b00000010)
bor_reset = bool(status_code_msb & 0b00000100)
ota = bool(status_code_msb & 0b00001000)
rtc_update = bool(status_code_msb & 0b00010000)
error_flag = bool(status_code_msb & 0b00100000)

print("header_version (MSB):", header_version_msb)
print("header_version (LSB):", header_version_lsb)
print("status code (MSB):", status_code_msb)
print("status code (LSB):", status_code_lsb)
print("sensor start:", sensor_start)
print("watchdog:", watchdog)
print("BOR reset:", bor_reset)
print("OTA:", ota)
print("RTC update:", rtc_update)
print("error flag:", error_flag)
