CXX = g++
CXXFLAGS = -O2 -std=c++17

COMMON = common/csr.cpp
COMMON_INC = -Icommon

ASSIGNMENT_02_INC = -Icommon -Iassignment_02/src
ASSIGNMENT_03_INC = -Icommon -Iassignment_03/src

all: wrapper \
     assignment_01/driver/gemm_driver \
     assignment_02/driver/bellman_ford_driver \
     assignment_02/driver/floyd_warshall_driver \
     assignment_03/driver/mst_driver


wrapper: common_wrapper/wrapper.cpp
	$(CXX) $(CXXFLAGS) common_wrapper/wrapper.cpp -o wrapper


assignment_01/driver/gemm_driver: \
	assignment_01/driver/driver.cpp \
	assignment_01/src/gemm.cpp
	$(CXX) $(CXXFLAGS) \
	assignment_01/driver/driver.cpp \
	assignment_01/src/gemm.cpp \
	-o assignment_01/driver/gemm_driver


assignment_02/driver/bellman_ford_driver: \
	$(COMMON) \
	assignment_02/src/bellman_ford.cpp \
	assignment_02/driver/bellman_ford_driver.cpp
	$(CXX) $(CXXFLAGS) $(ASSIGNMENT_02_INC) \
	$(COMMON) \
	assignment_02/src/bellman_ford.cpp \
	assignment_02/driver/bellman_ford_driver.cpp \
	-o assignment_02/driver/bellman_ford_driver


assignment_02/driver/floyd_warshall_driver: \
	assignment_02/src/floyd_warshall.cpp \
	assignment_02/driver/floyd_warshall_driver.cpp
	$(CXX) $(CXXFLAGS) $(ASSIGNMENT_02_INC) \
	assignment_02/src/floyd_warshall.cpp \
	assignment_02/driver/floyd_warshall_driver.cpp \
	-o assignment_02/driver/floyd_warshall_driver


assignment_03/driver/mst_driver: \
	$(COMMON) \
	assignment_03/src/mst.cpp \
	assignment_03/driver/mst_driver.cpp
	$(CXX) $(CXXFLAGS) $(ASSIGNMENT_03_INC) \
	$(COMMON) \
	assignment_03/src/mst.cpp \
	assignment_03/driver/mst_driver.cpp \
	-o assignment_03/driver/mst_driver


clean:
	rm -f wrapper
	rm -f assignment_01/driver/gemm_driver
	rm -f assignment_01/tests/csr_test
	rm -f assignment_02/driver/bellman_ford_driver
	rm -f assignment_02/driver/floyd_warshall_driver
	rm -f assignment_03/driver/mst_driver
