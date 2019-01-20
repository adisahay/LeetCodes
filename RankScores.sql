select orig.Score, groups.Rank from
(select Score, floor(@rno := @rno + 1) as Rank from
(select Score from Scores
group by Score
order by Score desc) Ranks
join (select @rno := 0) r) groups

right join (select Score from Scores
order by Score desc) orig
on orig.Score = groups.Score;
