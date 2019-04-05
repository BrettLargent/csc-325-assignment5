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
std::vector<int> input_vector;
std::map<int, std::map<int, int>> input;
int input_start_vertex;

// function declarations
void getInfo();


/*********************************************************************************
***MAIN FUNCTION for friend circle program****************************************
*********************************************************************************/
int main(){
    getInfo();
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
        char comma;
        std::istringstream iss(line);
        iss >> start_vertex;
        while(iss >> end_vertex >> comma >> weight) {
            input_vector.push_back(end_vertex);
            input_vector.push_back(weight);
            // std::map<pair<start_vertex, std::map<pair<end_vertex, weight>>> input;
        }
    }
    for (int i = 0; i < input_vector.size(); i++) 
        std::cout << input_vector.at(i) << " ";
    inFile.close();
}