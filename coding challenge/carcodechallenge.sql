create database virtualart
use virtualart

create table Artists (
ArtistID INT PRIMARY KEY,
Name VARCHAR(255) NOT NULL,
Biography TEXT,
Nationality VARCHAR(100));

select*from artists

create table Categories (
CategoryID INT PRIMARY KEY,
Name VARCHAR(100) NOT NULL);
select* from categories

create table Artworks (
ArtworkID INT PRIMARY KEY,
Title VARCHAR(255) NOT NULL,
ArtistID INT FOREIGN KEY references Artists(ArtistID),
CategoryID INT FOREIGN KEY references Categories(CategoryID),
Year INT,
Description TEXT,
ImageURL VARCHAR(255));
select*from artworks

create table Exhibitions (
ExhibitionID INT PRIMARY KEY,
Title VARCHAR(255) NOT NULL,
StartDate DATE,
EndDate DATE,
Description TEXT);
select*from exhibitions

create table ExhibitionArtworks (
ExhibitionID INT,
ArtworkID INT,
PRIMARY KEY (ExhibitionID, ArtworkID),
FOREIGN KEY (ExhibitionID) REFERENCES Exhibitions (ExhibitionID),
FOREIGN KEY (ArtworkID) REFERENCES Artworks (ArtworkID));
select*from ExhibitionArtworks

INSERT INTO Artists (ArtistID, Name, Biography, Nationality) VALUES
(1, 'Pablo Picasso', 'Renowned Spanish painter and sculptor.', 'Spanish'),
(2, 'Vincent van Gogh', 'Dutch post-impressionist painter.', 'Dutch'),
(3, 'Leonardo da Vinci', 'Italian polymath of the Renaissance.', 'Italian');

INSERT INTO Categories (CategoryID, Name) VALUES
(1, 'Painting'),
(2, 'Sculpture'),
(3, 'Photography');

INSERT INTO Artworks (ArtworkID, Title, ArtistID, CategoryID, Year, Description, ImageURL) VALUES
(1, 'Starry Night', 2, 1, 1889, 'A famous painting by Vincent van Gogh.', 'starry_night.jpg'),
(2, 'Mona Lisa', 3, 1, 1503, 'The iconic portrait by Leonardo da Vinci.', 'mona_lisa.jpg'),
(3, 'Guernica', 1, 1, 1937, 'Pablo Picassos powerful anti-war mural.', 'guernica.jpg');

INSERT INTO Exhibitions (ExhibitionID, Title, StartDate, EndDate, Description) VALUES
(1, 'Modern Art Masterpieces', '2023-01-01', '2023-03-01', 'A collection of modern art masterpieces.'),
(2, 'Renaissance Art', '2023-04-01', '2023-06-01', 'A showcase of Renaissance art treasures.');

INSERT INTO ExhibitionArtworks (ExhibitionID, ArtworkID) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2);

/*q1===Retrieve the names of all artists along with the number of artworks they have in the gallery, and
list them in descending order of the number of artworks.*/

select a.name,count(ar.artworkid) as no_of_artworks from Artists a join Artworks ar
on a.ArtistID=ar.ArtistID
group by a.name order by no_of_artworks desc;

/*q2===the titles of artworks created by artists from 'Spanish' and 'Dutch' nationalities, and order
them by the year in ascending order.*/

select ar.title from Artworks ar join Artists a on ar.ArtistID=a.ArtistID where a.Nationality in('spanish','dutch') 
order by ar.Year asc;

/*the names of all artists who have artworks in the 'Painting' category, and the number of
artworks they have in this category.*/

select a.name, count(*) as count_of_arts from artists a
join artworks aw on a.artistid = aw.artistid
join categories c on aw.categoryid = c.categoryid

group by a.name;


