        alert('Hello world');
        const data = '{{ qs_json }}'
        console.log(data)
        const rdata=JSON.parse(data.replace(/&quot;/g,''''))
        console.(rdata)
        const input= document.getElementById('search-here')
        console.log(input)
        let filteredArr=[]
        input.addEventListener('keyup', (e)=>{
        box.innerHTML=""
        filteredArr= rdata.filter(tweet=> tweet['text'].includes(e.target.value))
        console.log(filteredArr)
        if (filteredArr.length > 0)
        {filteredArr.map( tweet=>
        {box.innerHTML += '<b>${item['name']}</b><br>'})}
        else {box.innerHTML=<b> No result find </b>}
