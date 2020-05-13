
var fs = require('fs');
fs.readFile('./x-ori-HPL-1.out', 'utf8', function (err, data) {
    /**
     * 
     * @param {String} line 
     */
    function getBlock(line) {
        line.substr(0, 8);

        let ms = line.split(/\s+/);
        return {
            id: ms[0],
            N:ms[1],
            NB:ms[2],
            P:ms[3],
            Q:ms[4],
            Time:ms[5],
            Gflops:ms[6]
        }
    }
    let lines = data.split("\n").filter(e => e.length > 0 && e[0] == "W").map(e=>getBlock(e));
    // console.log(lines.map(e=>getBlock(e)).join("\n"));
    let mapper = {};
    lines.map(e => {
        let idx = `${e.N}-${e.NB}-${e.P}-${e.Q}`;
        if (mapper[idx] == undefined)
            mapper[idx] = []
        mapper[idx].push(e.Gflops);
        return e;
    });
    for (let k in mapper) {
        mapper[k].sort((a, b) => {
            if (a.split("e")[1] != b.split("e")[1])
                return parseFloat(a.split("e")[1]) < parseFloat(b.split("e")[1]);
            return parseFloat(a.split("e")[0]) < parseFloat(b.split("e")[0]);
        });
        console.log(`${k}: ${mapper[k][0]}`);
        
    }
});
