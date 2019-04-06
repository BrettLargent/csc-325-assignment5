/***************************************************
** CSC 325 - Assignment 5
** Dijkstra's Single Source Shortest Path Algorithm
** Authors: Lauren Tallerico
**          Brett Largent
**          Rich Russell
***************************************************/

#include<vector>
#include<iostream>
#include<fstream>
#include<iomanip>
#include<string>
#include<map>

// global variables
std::map<int, std::vector<int>> data;
int input_start_vertex;

// function declarations
void getInfo();
void checkData();

/*********************************************************************************
***MAIN FUNCTION for Dijkstra's shortest path*************************************
*********************************************************************************/
int main(){
    getInfo();
    checkData();
    return 0;
}

/*********************************************************************************
***Get user input for filename****************************************************
*********************************************************************************/
void getInfo(){
    std::ifstream inFile;
    std::string fileName;
    std::string line;
    std::cout << "Please provide a filename containing an adjacency list:" << std::endl;
    std::cin >> fileName;
    std::cout << "Please provide a start vertex Label (1..n):" << std::endl;
    std::cin >> input_start_vertex;
    inFile.open(fileName, std::ios::in);
    if (!inFile){
        std::cerr << "Can't open input file " << fileName << std::endl;
        exit(1);
    }
    while (std::getline(inFile, line)) {
        int start_vertex, end_vertex, weight;
        char comma, ws;
        std::istringstream iss(line);
        iss >> start_vertex;
        std::cout << std::endl;
        std::vector<int> vec;
        while(iss >> end_vertex >> comma >> weight) {
            vec.push_back(end_vertex);
            vec.push_back(weight);
            // data.insert(std::pair<int, std::vector<int> 
            //           >(start_vertex, {end_vertex, weight}));
        }
        data.insert(std::make_pair(start_vertex, vec));
    }
    inFile.close();
}

void checkData(){
    for(auto ii=data.begin(); ii!=data.end(); ++ii){
        std::cout << (*ii).first << ": ";
        std::vector <int> inVect = (*ii).second;
        for (unsigned j=0; j < inVect.size(); j++){
            std::cout << inVect.at(j) << " ";
        }
        std::cout << std::endl;
    }
}