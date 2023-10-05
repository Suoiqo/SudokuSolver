
window.addEventListener('DOMContentLoaded', event =>{

    //function creating normal td to display answer
    function create_block_empty(tr, tbody, i, pom){
        for (let j=0; j < 3; j++){
            let tdID = String(i) + String(j + pom);
            var td = document.createElement('td');
            td.className = "answer_normal";
            td.setAttribute("name", tdID);
            tr.appendChild(td);
        }
    };
    
    //function creating bold bordered td to display answer
    function create_block_bold(tr, tbody, i, pom){
        for (let j=0; j < 3; j++){
            let tdID = String(i) + String(j+pom);
            var td = document.createElement('td');
            td.className = "answer_block";
            td.setAttribute("name", tdID);
            tr.appendChild(td);
        }
    };

    //function creating normal td and input
    function create_input_block_empty(tr, tbody, i, pom){
        for (let j=0; j < 3; j++){
            let tdID = String(i) + String(j + pom);
            var td = document.createElement('td');
            td.className = "normal";
            td.setAttribute("name", tdID);
            var inp = document.createElement('input');
            inp.type = "text";
            inp.maxLength = "1";
            inp.size = "1";
            inp.style.textAlign = "center";
            inp.style.fontSize = "20px";
            inp.pattern = "[1-9]";
            inp.setAttribute("name", tdID);
            td.appendChild(inp);
            tr.appendChild(td);
        }
    };
    
    //function creating bold td and input
    function create_input_block_bold(tr, tbody, i, pom){
        for (let j=0; j < 3; j++){
            let tdID = String(i) + String(j+pom);
            var td = document.createElement('td');
            td.className = "block";
            td.setAttribute("name", tdID);
            var inp = document.createElement('input');
            inp.type = "text";
            inp.maxLength = "1";
            inp.size = "1";
            inp.style.textAlign = "center";
            inp.style.fontSize = "20px";
            inp.pattern = "[1-9]";
            inp.setAttribute("name", tdID);
            td.appendChild(inp)
            tr.appendChild(td);
        }
    };

    //show input table
    var sudokuDiv = document.getElementsByClassName('sudoku_input')[0];
    if(sudokuDiv){
        var table = document.createElement('table');
        var tbody = document.createElement('tbody');
        //creating 9x9 table
        for (let i=0; i < 9; i++){
            var tr = document.createElement('tr');
            if (i > 2 && i < 6){
                create_input_block_bold(tr, tbody, i, 0);
                create_input_block_empty(tr, tbody, i, 3);
                create_input_block_bold(tr, tbody, i, 6);
                tbody.appendChild(tr);
            }else{
                create_input_block_empty(tr, tbody, i, 0);
                create_input_block_bold(tr, tbody, i, 3);
                create_input_block_empty(tr, tbody, i, 6);
                tbody.appendChild(tr);
            }

        }
        table.appendChild(tbody);
        sudokuDiv.appendChild(table)
    }

    //show answer table
    var sudokuAnswerDiv = document.getElementsByClassName('sudoku_answer')[0];
    if(sudokuAnswerDiv){
        var answer_table = document.createElement('table');
        var answer_tbody = document.createElement('tbody');
        //creating 9x9 table
        for (let i=0; i < 9; i++){
            var tr = document.createElement('tr');
            if (i > 2 && i < 6){
                create_block_bold(tr, answer_tbody, i, 0);
                create_block_empty(tr, answer_tbody, i, 3);
                create_block_bold(tr, answer_tbody, i, 6);
                answer_tbody.appendChild(tr);
            }else{
                create_block_empty(tr, answer_tbody, i, 0);
                create_block_bold(tr, answer_tbody, i, 3);
                create_block_empty(tr, answer_tbody, i, 6);
                answer_tbody.appendChild(tr);
            }
        
        }
        answer_table.appendChild(answer_tbody);
        sudokuAnswerDiv.appendChild(answer_table)
    }
})



