const searchInput = document.getElementById("search");
const statusFilter = document.getElementById("status-filter");
const locationFilter = document.getElementById("location-filter");
const sortFilter = document.getElementById("sort");
const applicationCount = document.getElementById("applicationCount");

searchInput.addEventListener("keyup", filterInternships);
statusFilter.addEventListener("change", filterInternships);
locationFilter.addEventListener("change", filterInternships);
sortFilter.addEventListener("change", filterInternships);

function filterInternships() {

    const searchText = searchInput.value.toLowerCase();

    const selectedStatus = statusFilter.value;

    const selectedLocation = locationFilter.value;

    let cards = Array.from(document.querySelectorAll(".searchable-card"));

    cards.forEach(function(card){

        const company = card
            .querySelector(".company-name")
            .textContent
            .toLowerCase();

        const role = card
            .querySelector(".role-name")
            .textContent
            .toLowerCase();

        const status = card
            .querySelector(".internship-status")
            .textContent
            .trim();

        const location = card
            .querySelector(".internship-location")
            .textContent
            .trim();

        const searchMatch =
            company.includes(searchText) ||
            role.includes(searchText);

        const statusMatch =
            selectedStatus === "all" ||
            selectedStatus === status;

        const locationMatch =
            selectedLocation === "all" ||
            selectedLocation === location;

        if(searchMatch && statusMatch && locationMatch){

            card.style.display = "block";

        }else{

            card.style.display = "none";

        }

    });

    sortCards();

    updateCount();

}

function sortCards(){

    const container = document.querySelector(".internship-list");

    let cards = Array.from(document.querySelectorAll(".searchable-card"));

    cards.sort(function(a,b){

        const dateA = new Date(
            a.querySelector(".application-date").textContent
        );

        const dateB = new Date(
            b.querySelector(".application-date").textContent
        );

        const deadlineA = new Date(
            a.querySelector(".deadline-date").textContent
        );

        const deadlineB = new Date(
            b.querySelector(".deadline-date").textContent
        );

        if(sortFilter.value === "newest"){

            return dateB-dateA;

        }

        if(sortFilter.value === "oldest"){

            return dateA-dateB;

        }

        if(sortFilter.value === "deadline"){

            return deadlineA-deadlineB;

        }

    });

    cards.forEach(function(card){

        container.appendChild(card);

    });

}

function updateCount(){

    const cards = document.querySelectorAll(".searchable-card");

    let visible = 0;

    cards.forEach(function(card){

        if(card.style.display !== "none"){

            visible++;

        }

    });

    applicationCount.textContent =
        `${visible} of ${cards.length} shown`;

}   