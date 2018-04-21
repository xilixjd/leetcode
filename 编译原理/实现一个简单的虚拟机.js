/**
 * Created by xilixjd on 18/4/15.
 */

// https://www.zhihu.com/question/33084689

function inst_t(code, cond, p1, p2) {
	this.code = code;
	this.cond = cond;
	this.p1 = p1;
	this.p2 = p2;
}

function vm_state_t(ip, flag, code, data) {
	this.ip = ip || 0;
	this.flag = flag;
	this.code = code || new inst_t();
	this.data = data;
}

IADD = 1
ISUB = 2
ICMP = 3
IJMP = 4
IMOV = 5
ISTIP = 6
ILDIP = 7
ILD = 8
IOUT = 9
ISTOP = 255
FNA = 0
FEQ = 1
FNE = 2

function execute(state) {
	while (true) {
		current = state.code[state.ip];
		state.ip += 1;
		if (current.cond != FNA && current.cond != state.flag) {
			continue;
		}
		switch (current.code) {
            case IADD:
				state.data[current.p1] += state.data[current.p2];
				break;
            case ISUB:
				state.data[current.p1] -= state.data[current.p2];
            case ICMP:
				if (state.data[current.p1] == state.data[current.p2]) {
					state.flag = FEQ;
				} else {
					state.flag = FNE;
				}
				break;
            case IJMP:
				state.ip += current.p1;
				break;
            case IMOV:
				state.data[current.p1] = state.data[current.p2];
				break;
            case ISTIP:
				state.data[current.p1] = state.ip;
				break;
            case ILDIP:
				state.ip = state.data[current.p1];
				break;
            case ILD:
				state.data[current.p1] = current.p2;
				break;
            case IOUT:
				console.log(state.data[current.p1]);
				break;
            case ISTOP:
				return;
		}
	}
}
data = []

sample_code = [new inst_t(ILD, FNA, 2, 100), new inst_t(ILD, FNA, 3, 1),
    new inst_t(ILD, FNA, 1, 1), new inst_t(ILD, FNA, 0, 0), new inst_t(ICMP, FNA, 1, 2),
    new inst_t(IJMP, FEQ, 3, 0), new inst_t(IADD, FNA, 0, 1), new inst_t(IADD, FNA, 1, 3),
    new inst_t(IJMP, FNA, -5, 0), new inst_t(IOUT, FNA, 0, 0), new inst_t(ISTOP, FNA, 0, 0)]

state = new vm_state_t()

state.code = sample_code

state.data = data

execute(state)