USB_VID = 0x303A
USB_PID = 0x8204
USB_PRODUCT = "ThingPulse Pendrive S3"
USB_MANUFACTURER = "ThingPulse"

IDF_TARGET = esp32s3

CIRCUITPY_ESP_FLASH_SIZE = 4MB
CIRCUITPY_ESP_FLASH_MODE = qio
CIRCUITPY_ESP_FLASH_FREQ = 80m

CIRCUITPY_ESP_PSRAM_SIZE = 2MB
CIRCUITPY_ESP_PSRAM_MODE = qio
CIRCUITPY_ESP_PSRAM_FREQ = 80m

CIRCUITPY_ESPCAMERA = 0
CIRCUITPY_DISPLAYIO = 1

FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
