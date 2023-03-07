let idCount = 0;

const tags = {
  'H2': 0,
  'H3': 1,
  'H4': 2, 
};

const postContent = document.querySelector('.tt_article_useless_p_margin');
const headings = postContent.querySelectorAll('h2, h3, h4[data-ke-size]');
const filteredHeadings = [...headings].filter(heading => heading.textContent.trim());
const minHeadingNumber = Math.min.apply(null, filteredHeadings.map(heading => tags[heading.tagName]));


const generateID = () => `heading${idCount++}`;
const calcTagNumber = (tagName) => tags[tagName] - minHeadingNumber;

const tocContents = filteredHeadings.reduce((prev, cur, idx) => {
  const headingTagName = cur.tagName;
  const headingText = cur.textContent;
  const headingID = generateID();
  
  const newHeadingHTML = `
  <li data-tag="${calcTagNumber(headingTagName)}">
    <a href="#${headingID}">${headingText}</a>
  </li>`;
  
  cur.id = headingID;
  return prev + newHeadingHTML;
}, '');

if (filteredHeadings.length) {
  const tocWrapper = `
  <section class="toc on">
    <div class="toc-header">
      <svg class="toc-icon" xmlns="http://www.w3.org/2000/svg" width="36px" height="36px" viewBox="0 0 91 91" 
        enable-background="new 0 0 91 91">
        <rect height="3.4" width="30.602" x="36.891" y="31.362"/>
        <rect height="3.4" width="30.602" x="36.891" y="44.962"/>
        <rect height="3.4" width="30.602" x="36.891" y="58.562"/>
        <path d="M27.594,36.462c1.877,0,3.398-1.522,3.398-3.4c0-1.877-1.521-3.399-3.398-3.399h-0.02c-1.877,0-3.391,1.522-3.391,3.399   
        C24.184,34.939,25.715,36.462,27.594,36.462z"/>
        <path d="M27.594,50.062c1.877,0,3.398-1.521,3.398-3.399s-1.521-3.399-3.398-3.399h-0.02c-1.877,0-3.391,1.521-3.391,3.399   
        S25.715,50.062,27.594,50.062z"/>
        <path 
      d="M27.594,63.662c1.877,0,3.398-1.522,3.398-3.399c0-1.879-1.521-3.4-3.398-3.4h-0.02c-1.877,0-3.391,1.521-3.391,3.4   
      C24.184,62.14,25.715,63.662,27.594,63.662z"/>
      </svg>
      <span>목차</span>
      <button class="toggle-btn">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" 
        viewBox="0 0 24 24" version="1.1">
            <path d="M 18.804688 15.898438 L 12 8.894531 L 5.195312 15.898438 L 4.800781 15.515625 L 12 8.101562 L 19.199219 
            15.515625 Z M 18.804688 15.898438 " stroke="#111"></path>
        </svg>
      </button>
    </div>
    <div class="toc-body">
      <ul class="toc-list">${tocContents}</ul>
    </div>
  </section>
  <div class="toc-right">
    <div class="toc-header">
      <button class="toggle-btn">
        <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24px" height="24px" 
          viewBox="0 0 24 24" version="1.1">
          <path style=" stroke:none;fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;" d="M 15.898438 5.195312 L 8.890625 12 
            L 15.898438 18.804688 L 15.511719 19.199219 L 8.101562 12 L 15.511719 4.800781 Z M 15.898438 5.195312 "/>
        </svg>
      </button>
    </div>
    <div class="toc-body">
      <ul class="toc-list">${tocContents}</ul>
    </div>
  </div>
  `;

  postContent.insertAdjacentHTML('afterbegin', tocWrapper);

  const toc = postContent.querySelector('.toc');
  const rightToc = postContent.querySelector('.toc-right');

  const tocToggleBtn = toc.querySelector('.toggle-btn');
  const handleTocToggle = () => {
    toc.classList.toggle('on');
  };
  tocToggleBtn.addEventListener('click', handleTocToggle);

  const rightTocToggleBtn = rightToc.querySelector('.toggle-btn');
  const handleRightTocToggle = () => {
    rightToc.classList.toggle('on');
  };
  rightTocToggleBtn.addEventListener('click', handleRightTocToggle);

  const handleTocClick = (event) => {
    event.preventDefault();
    const targetHeadingID = event.target.getAttribute('href');
    const target = document.querySelector(targetHeadingID);
    target?.scrollIntoView({ behavior: 'smooth' });
  };
  toc.addEventListener('click', handleTocClick);
  rightToc.addEventListener('click', handleTocClick);

  const handleTocScroll = ([entries]) => {
    const isTocVisible = entries.isIntersecting;
    const rootWidth = document.body.offsetWidth;

    if (rootWidth > 1600) {
      isTocVisible ? rightToc.classList.remove('on') : rightToc.classList.add('on');
    }
  };

  const tocObserver = new IntersectionObserver(handleTocScroll);
  tocObserver.observe(toc);

  const rightTocElements = rightToc.querySelectorAll('li a');
  const handleRightTocScroll = ([entry]) => {
    const { target, isIntersecting, boundingClientRect, intersectionRatio } = entry;
    if (entry.isIntersecting) {  
      const targetID = entry.target.id;
      rightTocElements.forEach(heading => {
        if (heading.href.endsWith(targetID)) {
          heading.classList.add('active');
          return;
        }
        heading.classList.remove('active');
      });
    }
  };

  const headingObserver = new IntersectionObserver(handleRightTocScroll, {
    rootMargin: '0px 0px -90% 0px',
  });
  for (const heading of filteredHeadings) {
    headingObserver.observe(heading);
  }
}


const menu = document.querySelector(".menu-list");
const menuBtn = document.querySelector(".menu-btn");
const cancelBtn = document.querySelector(".cancel-btn");

menuBtn.onclick = ()=>{
  menu.classList.add("active");
  menuBtn.classList.add("hide");
}

cancelBtn.onclick = ()=>{
  menu.classList.remove("active");
  menuBtn.classList.remove("hide");
}