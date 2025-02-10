// This file is part of the CircuitPython project: https://circuitpython.org
//
// SPDX-FileCopyrightText: Copyright (c) 2019 Lucian Copeland for Adafruit Industries
//
// SPDX-License-Identifier: MIT

#pragma once

// I2C
#define I2C_BANK_ARRAY_LEN  3
#define I2C_SDA_ARRAY_LEN   6
#define I2C_SCL_ARRAY_LEN   4
extern I2C_TypeDef *mcu_i2c_banks[I2C_BANK_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_i2c_sda_list[I2C_SDA_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_i2c_scl_list[I2C_SCL_ARRAY_LEN];


// SPI
#define SPI_BANK_ARRAY_LEN  5
#define SPI_SCK_ARRAY_LEN   8
#define SPI_MOSI_ARRAY_LEN  7
#define SPI_MISO_ARRAY_LEN  6
#define SPI_NSS_ARRAY_LEN   8
extern SPI_TypeDef *mcu_spi_banks[SPI_BANK_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_spi_sck_list[SPI_SCK_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_spi_mosi_list[SPI_MOSI_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_spi_miso_list[SPI_MISO_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_spi_nss_list[SPI_NSS_ARRAY_LEN];

// UART
#define UART_TX_ARRAY_LEN   6
#define UART_RX_ARRAY_LEN   5
extern USART_TypeDef *mcu_uart_banks[MAX_UART];
extern bool mcu_uart_has_usart[MAX_UART];
extern const mcu_periph_obj_t mcu_uart_tx_list[UART_TX_ARRAY_LEN];
extern const mcu_periph_obj_t mcu_uart_rx_list[UART_RX_ARRAY_LEN];

// Timers
#define TIM_BANK_ARRAY_LEN  14
#define TIM_PIN_ARRAY_LEN   34
extern TIM_TypeDef *mcu_tim_banks[TIM_BANK_ARRAY_LEN];
extern const mcu_tim_pin_obj_t mcu_tim_pin_list[TIM_PIN_ARRAY_LEN];
