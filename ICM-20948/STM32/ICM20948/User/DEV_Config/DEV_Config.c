/*****************************************************************************
* | File      	:   DEV_Config.c
* | Author      :   Waveshare team
* | Function    :   Hardware underlying interface
* | Info        :
*                Used to shield the underlying layers of each master 
*                and enhance portability
*----------------
* |	This version:   V1.0
* | Date        :   2018-11-22
* | Info        :

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
******************************************************************************/
#include "DEV_Config.h"
UWORD IIC_Addr_t = IIC_Addr; 


void DEV_Set_I2CAddress(UBYTE add_)
{
	IIC_Addr_t = add_;
}

/******************************************************************************
function:	
	I2C Write and Read
******************************************************************************/
void DEV_I2C_WriteByte(UBYTE add_, UBYTE data_)
{
	UBYTE Buf[1] = {0};
	Buf[0] = data_;
	HAL_I2C_Mem_Write(&hi2c1, IIC_Addr_t, add_, I2C_MEMADD_SIZE_8BIT, Buf, 1, 0x10);
}

void DEV_I2C_WriteWord(UBYTE add_, UWORD data_)
{
	UBYTE Buf[2] = {0};
	Buf[0] = data_ >> 8; 
	Buf[1] = data_;
	HAL_I2C_Mem_Write(&hi2c1, IIC_Addr_t, add_, I2C_MEMADD_SIZE_8BIT, Buf, 2, 0x10);
}

UBYTE DEV_I2C_ReadByte(UBYTE add_)
{
	UBYTE Buf[1]={add_};
	HAL_I2C_Mem_Read(&hi2c1, IIC_Addr_t, add_, I2C_MEMADD_SIZE_8BIT, Buf, 1, 0x10);
	return Buf[0];
}

UWORD DEV_I2C_ReadWord(UBYTE add_)
{
    UBYTE Buf[2]={0, 0};
		HAL_I2C_Mem_Read(&hi2c1, IIC_Addr_t, add_, I2C_MEMADD_SIZE_8BIT, Buf, 2, 0x10);
    return ((Buf[0] << 8) | (Buf[1] & 0xff));
}

/******************************************************************************
function:	
			Redefine printf    --UART2
******************************************************************************/
int fputc(int ch, FILE *f)
{
	HAL_UART_Transmit(&huart2, (uint8_t *)&ch, 1, 0xFFFF);
	return ch;
}







