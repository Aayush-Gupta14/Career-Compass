const searchInput = document.getElementById("searchInput");
const difficultyFilter = document.getElementById("difficultyFilter");
const topicFilter = document.getElementById("topicFilter");
const statusFilter = document.getElementById("statusFilter");
const problemCount = document.getElementById("problemCount");

searchInput.addEventListener("keyup", filterProblems);
difficultyFilter.addEventListener("change", filterProblems);
topicFilter.addEventListener("change", filterProblems);
statusFilter.addEventListener("change", filterProblems);

function filterProblems() {

    const searchText = searchInput.value.toLowerCase();
    const selectedDifficulty = difficultyFilter.value;
    const selectedTopic = topicFilter.value;
    const selectedStatus = statusFilter.value;

    const cards = document.querySelectorAll(".problem-card");

    let visibleCards = 0;

    cards.forEach(function(card) {

        const problemName = card
            .querySelector(".problem-name")
            .textContent
            .toLowerCase();

        const cardDifficulty = card
            .querySelector(".problem-difficulty")
            .textContent
            .trim();

        const cardTopic = card
            .querySelector(".problem-topic")
            .textContent
            .trim();

        const cardStatus = card
            .querySelector(".problem-status")
            .textContent
            .trim();

        const searchMatch = problemName.includes(searchText);

        const difficultyMatch =
            selectedDifficulty === "All Difficulty" ||
            selectedDifficulty === cardDifficulty;

        const topicMatch =
            selectedTopic === "All Topics" ||
            selectedTopic === cardTopic;

        const statusMatch =
            selectedStatus === "All Status" ||
            selectedStatus === cardStatus;

        if (
            searchMatch &&
            difficultyMatch &&
            topicMatch &&
            statusMatch
        ) {
            card.style.display = "block";
            visibleCards++;
        } else {
            card.style.display = "none";
        }

    });

    problemCount.textContent = `${visibleCards} of ${cards.length} shown`;

}
