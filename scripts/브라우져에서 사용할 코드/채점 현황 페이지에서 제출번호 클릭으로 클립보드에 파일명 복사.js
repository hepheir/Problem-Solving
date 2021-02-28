javascript: (() => {
    const option = {
        includesMemoryOnCorrect: true,
        includesTimeOnCorrect: true,
        
        includesExt: false,

        useClipboard: true,
        useAlert: false,

        showDatetimeUsingAlert: true,
    };

    function onClick(event) {
        const statusTableRow = event.target.parentNode.parentNode;
        const cells = statusTableRow.getElementsByTagName('td');
        const result = {
            id: cells[1].innerText,
            user: cells[2].innerText,
            problem: cells[3].innerText,
            verdict : cells[4].innerText,
            memory: cells[5].innerText,
            time: cells[6].innerText,
            language: cells[7].innerText,
            length: cells[8].innerText,
            datetime: cells[9].children[0].getAttribute('data-original-title'),
        };
        const data = [ result.id, result.verdict ];
        var filename = '';
        var ext = '';

        if (option.includesMemoryOnCorrect) data.push(result.memory+' KB');
        if (option.includesTimeOnCorrect) data.push(result.time+' ms');
        if (option.includesExt) {
            if (result.language.includes('Python') || result.language.includes('PyPy3')) {
                ext = '.py';
            } else if (result.language.includes('Java 11')) {
                ext = '.java';
            } else if (result.language.includes('C++')) {
                ext = '.cpp';
            }
        }

        filename = data.join(' ') + ext;

        if (option.useClipboard) navigator.clipboard.writeText(filename);
        if (option.useAlert) alert(filename);

        if (option.showDatetimeUsingAlert) alert(result.datetime);
    }

    const solution = document.getElementById('status-table').getElementsByTagName('tr');
    for (let i=0; i<solution.length; i++) {
        const celltype = (i == 0) ? 'th' : 'td';
        const cell = document.createElement(celltype);

        if (i == 0) {
            cell.innerHTML = '파일명 생성';
        } else {
            const button = document.createElement('button');

            button.style.borderRadius = '3px';
            button.style.color = '#fff';
            button.style.backgroundColor = '#3071a9';
            button.style.borderColor = '#285e8e';
            button.style.padding = '5px 10px';
            button.style.fontSize = '12px';
            button.style.lineHeight = '1.5';
            button.innerHTML = '복사';
    
            button.addEventListener('click', onClick);
            cell.appendChild(button);
        }
        solution[i].insertBefore(cell, solution[i].getElementsByTagName(celltype)[0]);
    };
})();
