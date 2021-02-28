javascript: (() => {
    const solution = document.getElementById('status-table').getElementsByTagName('tr');
    for (let i=1; i<=20; i++) {
        const cells = solution[i].getElementsByTagName('td');
        cells[0].addEventListener('click', evt => {
            const id = cells[0].innerText;
            const verdict = cells[3].innerText;
            const memory = cells[4].innerText;
            const time = cells[5].innerText;
            
            var result = `${id} ${verdict}`;
            if (verdict  == '맞았습니다!!') {
                result += ` ${memory} KB ${time} ms`
            }
            navigator.clipboard.writeText(result);
        });
    };
    alert('제출 번호를 클릭해 보세요.');
})();