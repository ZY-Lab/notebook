centos7安装依赖库
安装centos系统依赖

yum install -y automake autoconf libtool gcc gcc-c++ 
yum install -y libpng-devel libjpeg-devel libtiff-devel
安装leptonica

wget http://www.leptonica.org/source/leptonica-1.72.tar.gz
tar xvzf leptonica-1.72.tar.gz
cd leptonica-1.72/ 
./configure 
make && make install
安装tesseract-ocr

wget https://github.com/tesseract-ocr/tesseract/archive/3.04.zip
unzip 3.04.zip
cd tesseract-3.04/ 
./configure
make && make install 
sudo ldconfig


## 4.0安装
1. 下载tesseract-ocr源码
git clone -b master https://github.com/tesseract-ocr/tesseract.git tesseract-ocr
2. 安装g++
yum?install?gcc?gcc-c++?make
3. 安装autoconf automake libtool libjpeg-devellibpng-devel libtiff-devel zlib-devel
yum install autoconf automake libtool
yum install libjpeg-devel libpng-devel libtiff-devel zlib-devel
4. 安装leptonica
wget http://www.leptonica.org/source/leptonica-1.76.0.tar.gz
解压后 进入目录后依次执行:
./configure
make
make install
编译完成后使用vim增加如下三个变量：
vim /etc/profile
export LD_LIBRARY_PATH=$LD_LIBRARY_PAYT:/usr/local/lib
export LIBLEPT_HEADERSDIR=/usr/local/include
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

保存后执行： source /etc/profile
5.???进入第1步下载的tesseract-ocr目录依次执行如下命令：
./autogen.sh
./configure
make
make install
6.???安装pytesseract
pip install pytesseract
