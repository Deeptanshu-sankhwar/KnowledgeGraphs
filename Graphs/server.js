    var express = require("express"); 
    var app = express(); 
    var path = require("path"); 
    //Faculty
    app.get('/faculty',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Faculty/index.html')); 
    });
    app.get('/faculty/position',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Faculty/Position.html')); 
    });
    app.get('/faculty/office',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Faculty/Office.html')); 
    });
    app.get('/faculty/domain',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Faculty/Domain.html')); 
    });
    app.get('/faculty/block',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Faculty/Block.html')); 
    }); 
  	app.get('/Scraper/Faculty',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Scraper/faculty.json')); 
    }); 
    
    //Publications
    app.get('/publications',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Publications/index.html')); 
    });
    app.get('/publications/authors',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Publications/Authors.html')); 
    });
    app.get('/publications/year',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Publications/Year.html')); 
    });
    app.get('/Scraper/Publications',function(req,res){ 
      res.sendFile(path.join(__dirname+'/Scraper/Publications.json')); 
    });

    app.listen(3000); 
    console.log("Server running at Port 3000"); 
