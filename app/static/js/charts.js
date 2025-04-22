// Will Nzeuton, Andy Shyklo, Kyle Lee, Margie Cao
// JOY ACROSS BORDERS 🔥🔥😵‍💫 by madeinguatemala
// SoftDev
// p04
// 2025-03-28

var score = {
    chart: {
        type: 'line',
        height: 500,
        width: "100%",
      },
    series: [{
        name: 'sales',
        data: Object.values(scoredata)
      }],
    xaxis: {
        categories: Object.keys(scoredata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var rank = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(rankdata)
      }],
    xaxis: {
        categories: Object.keys(rankdata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var free = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(freedata)
      }],
    xaxis: {
        categories: Object.keys(freedata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var heal = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(healthdata)
      }],
    xaxis: {
        categories: Object.keys(healthdata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var cor = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(cordata)
      }],
    xaxis: {
        categories: Object.keys(cordata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var gd = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(gdpdata)
      }],
    xaxis: {
        categories: Object.keys(gdpdata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var fam = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(famdata)
      }],
    xaxis: {
        categories: Object.keys(famdata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

var gen = {
    chart: {
        type: 'line'
      },
    series: [{
        name: 'sales',
        data: Object.values(gendata)
      }],
    xaxis: {
        categories: Object.keys(gendata)
    },
    stroke: {
        curve: 'smooth'
    },
    markers: {
        size: 5
    },
    yaxis: {
        forceNiceScale: true,
        decimalsInFloat: 2
    }
}

  var happyscore = new ApexCharts(document.querySelector("#happyscore"), score);
  var happyrank = new ApexCharts(document.querySelector("#happyrank"), rank);
  var freedom = new ApexCharts(document.querySelector("#freedom"), free);
  var health = new ApexCharts(document.querySelector("#health"), heal);
  var corruption = new ApexCharts(document.querySelector("#corruption"), cor);
  var gdp = new ApexCharts(document.querySelector("#gdp"), gd);
  var family = new ApexCharts(document.querySelector("#family"), fam);
  var generosity = new ApexCharts(document.querySelector("#generosity"), gen);

  happyscore.render();
  happyrank.render();
  freedom.render();
  health.render();
  corruption.render();
  gdp.render();
  family.render();
  generosity.render();