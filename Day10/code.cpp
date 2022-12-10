#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <array>

void task1_check_signal(int cycle, int x){
    static int total_signal = 0;
    if ((cycle - 20) % 40 == 0){
        total_signal += cycle*x;
        std::cout << "[" << cycle << "]\t" << "Singal Strength: " << cycle*x << "\tTotal: " << total_signal << std::endl;
    }
}

enum InstructionType{
    ADDX,
    NOOP,
};

struct Instruction {
    InstructionType type;
    int value;
};

const Instruction parse_instruction(std::string line){
    std::string type = line.substr(0, 4);
    int value = (line.size() > 4) ? std::stoi(line.substr(line.find(' '), std::string::npos)) : 0;

    if (type == "addx")
        return Instruction{ADDX, value};

    return Instruction{NOOP, 0};
}

class CRT{
    public:
        CRT() : x(40), y(6), screen{false} {};
        void update(int cycle, int x);
        void draw();
    private:
        int x, y;
        std::array<bool, 40*6> screen;
};

void CRT::update(int cycle, int sprite_pos){
    int mod_cycle = cycle % 40;
    if (sprite_pos == mod_cycle || sprite_pos - 1 == mod_cycle || sprite_pos + 1 == mod_cycle)
        screen[cycle] = true;
}

void CRT::draw(){
    for (int i = 0; i < x*y; i++){
        char c = screen[i] ? '#' : '.';
        std::cout << c;
        if ((i+1) % x == 0)
            std::cout << std::endl;
    }
}

class CPU {
    public:
        CPU(std::vector<Instruction> instructionStack) : 
            instructionStack(instructionStack), 
            registerX(1),
            cycle(0){};
        ~CPU(){};
        void execute();
    private:
        CRT screen;
        int registerX;
        unsigned int cycle;
        std::vector<Instruction> instructionStack;
        void increment_cycle();
};

void CPU::execute(){
    for (Instruction instruction : instructionStack){
        switch(instruction.type){
            case ADDX:
                increment_cycle();
                increment_cycle();
                registerX += instruction.value;
                break;
            case NOOP:
                increment_cycle();
                break;
        }
    }
}

void CPU::increment_cycle(){
    screen.update(cycle, registerX);
    cycle += 1;
    task1_check_signal(cycle, registerX);
    if (cycle == 240) screen.draw();
}

int main(int argc, char* argv[]) {
    if (argc < 2){
        std::cout << "Usage: ./code input.txt" << std::endl;
        return -1;
    }

    std::vector<Instruction> instructionStack;

    auto input_file = std::fstream(argv[1]);
    for (std::string line; std::getline(input_file, line);) {
        if (line.empty()) 
            continue;
        
        instructionStack.push_back(parse_instruction(line));
    }

    CPU cpu(instructionStack);
    cpu.execute();
    return 0;
}