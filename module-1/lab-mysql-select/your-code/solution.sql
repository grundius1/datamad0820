select  authors.au_id,au_lname,au_fname,title, pub_name
	from titles
	INNER join titleauthor on titles.title_id = titleauthor.title_id
	INNER Join authors on titleauthor.au_id = authors.au_id
	INNER join publishers on titles.pub_id = publishers.pub_id
    
    
    
    
select  
	authors.au_id,
	au_lname,
	au_fname,
    	pub_name,
    	count(pub_name) as TITLECOUNT
	from titles 
	INNER join titleauthor on titles.title_id = titleauthor.title_id
	INNER Join authors on titleauthor.au_id = authors.au_id
	INNER join publishers on titles.pub_id = publishers.pub_id
	group by pub_name, authors.au_id



select
	authors.au_id,
	authors.au_lname,
	authors.au_fname,
	sum(ytd_sales) as qty
	from sales
	left join titleauthor on sales.title_id = titleauthor.title_id
	left join authors on titleauthor.au_id = authors.au_id
	left join titles on sales.title_id = titles.title_id
	group by authors.au_id
	order by qty desc
	LIMIT 3
    
    
select
	authors.au_id,
	authors.au_lname,
	authors.au_fname,
	sum(sales.qty) qty
	from authors
	left join titleauthor on authors.au_id = titleauthor.au_id
	left join sales on titleauthor.title_id = sales.title_id
	group by authors.au_id
	order by qty desc
	
	
	
	
select 
	authors.au_id,
    authors.au_fname,
    authors.au_lname,
    sum(round(((titles.advance*(titleauthor.royaltyper/100)) + ((titles.price*(titles.royalty/100)*(titleauthor.royaltyper/100))*titles.ytd_sales)))) as profit     
	from titles
    left join titleauthor on titles.title_id = titleauthor.title_id
    left join authors on titleauthor.au_id = authors.au_id
    left join sales on titles.title_id = sales.title_id
    group by authors.au_id
    order by profit desc
    limit 3
