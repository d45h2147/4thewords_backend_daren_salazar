CREATE DATABASE IF NOT EXISTS 4thewords_prueba_daren_salazar_h;
USE 4thewords_prueba_daren_salazar_h;


CREATE TABLE IF NOT EXISTS province (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_province PRIMARY KEY (id) 
);


CREATE TABLE IF NOT EXISTS canton (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    province_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_canton PRIMARY KEY (id), 
    CONSTRAINT fk_canton_province FOREIGN KEY (province_id) REFERENCES province(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS district (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    canton_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_district PRIMARY KEY (id), 
    CONSTRAINT fk_district_canton FOREIGN KEY (canton_id) REFERENCES canton(id) ON DELETE CASCADE
);


CREATE TABLE IF NOT EXISTS category (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT pk_category PRIMARY KEY (id) 
);


CREATE TABLE IF NOT EXISTS legend (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    category_id INT NOT NULL,
    description TEXT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
    legend_date DATE NOT NULL,
    province_id INT NOT NULL,
    canton_id INT NOT NULL,
    district_id INT NOT NULL,
    image_url VARCHAR(500), 
    source VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    deleted_at TIMESTAMP NULL,
    CONSTRAINT pk_legend PRIMARY KEY (id), 
    CONSTRAINT fk_legend_category FOREIGN KEY (category_id) REFERENCES category(id) ON DELETE CASCADE,
    CONSTRAINT fk_legend_province FOREIGN KEY (province_id) REFERENCES province(id) ON DELETE CASCADE,
    CONSTRAINT fk_legend_canton FOREIGN KEY (canton_id) REFERENCES canton(id) ON DELETE CASCADE,
    CONSTRAINT fk_legend_district FOREIGN KEY (district_id) REFERENCES district(id) ON DELETE CASCADE
);

-- CREATE INDEX idx_province_name ON province(name);
-- CREATE INDEX idx_canton_name ON canton(name);
-- CREATE INDEX idx_district_name ON district(name);
-- CREATE INDEX idx_category_name ON category(name);

-- CREATE INDEX idx_legend_name ON legend(name);
-- CREATE INDEX idx_legend_date ON legend(legend_date);
-- CREATE INDEX idx_legend_category ON legend(category_id);
-- CREATE INDEX idx_legend_province ON legend(province_id);
-- CREATE INDEX idx_legend_canton ON legend(canton_id);
-- CREATE INDEX idx_legend_district ON legend(district_id);

SET NAMES utf8mb4;

INSERT INTO province (id, name) VALUES 
(1, _utf8mb4'San José'), 
(2, _utf8mb4'Alajuela'), 
(3, _utf8mb4'Cartago'),
(4, _utf8mb4'Heredia'), 
(5, _utf8mb4'Guanacaste'), 
(6, _utf8mb4'Puntarenas'), 
(7, _utf8mb4'Limón');

INSERT INTO canton (id, name, province_id) VALUES 
(1, _utf8mb4'San José', 1), 
(2, _utf8mb4'Alajuela', 2), 
(3, _utf8mb4'Cartago', 3),
(4, _utf8mb4'Heredia', 4), 
(5, _utf8mb4'Liberia', 5), 
(6, _utf8mb4'Puntarenas', 6), 
(7, _utf8mb4'Limón', 7);

INSERT INTO district (id, name, canton_id) VALUES 
(1, _utf8mb4'Carmen', 1), 
(2, _utf8mb4'Central', 2), 
(3, _utf8mb4'Oriental', 3),
(4, _utf8mb4'Mercedes', 4), 
(5, _utf8mb4'Liberia Centro', 5), 
(6, _utf8mb4'Barrio El Carmen', 6), 
(7, _utf8mb4'Valle La Estrella', 7);

INSERT INTO category (id, name) VALUES 
(1, _utf8mb4'Fantasmas'), 
(2, _utf8mb4'Criaturas'), 
(3, _utf8mb4'Mitos Históricos'),
(4, _utf8mb4'Brujería'), 
(5, _utf8mb4'Seres Míticos'), 
(6, _utf8mb4'Historias de Tesoros');

INSERT INTO legend (id, name, category_id, description, legend_date, province_id, canton_id, district_id, image_url, source) VALUES 
(4, _utf8mb4'La Tulevieja', 4, _utf8mb4'Mujer maldita con cuerpo de bruja y alas de ave.', '1900-01-01', 4, 4, 4, 'https://placehold.co/300x300', _utf8mb4'Relatos del Pueblo'), 
(5, _utf8mb4'El Padre sin Cabeza', 5, _utf8mb4'Espíritu de un sacerdote sin cabeza que aparece en la iglesia.', '1800-01-01', 5, 5, 5, 'https://placehold.co/300x300', _utf8mb4'Leyendas de Costa Rica'), 
(6, _utf8mb4'El Tesoro de la Isla del Coco', 6, _utf8mb4'Se dice que piratas enterraron grandes tesoros en la isla.', '1700-01-01', 6, 6, 6, 'https://placehold.co/300x300', _utf8mb4'Historias de Marineros'), 
(7, _utf8mb4'La Mona', 4, _utf8mb4'Mujer que se transforma en una criatura espeluznante por las noches.', '1950-01-01', 7, 7, 7, 'https://placehold.co/300x300', _utf8mb4'Tradiciones Populares'), 
(8, _utf8mb4'El Chingo', 5, _utf8mb4'Un niño fantasma sin piernas que aparece en los caminos.', '1930-01-01', 1, 1, 1, 'https://placehold.co/300x300', 'Relatos Antiguos'), 
(9, _utf8mb4'El Duende del Bosque', 5, _utf8mb4'Pequeño ser que protege los árboles y asusta a los leñadores.', '1890-01-01', 2, 2, 2, 'https://placehold.co/300x300', _utf8mb4'Mitos y Creencias'), 
(10, _utf8mb4'La Casa Embrujada de Cartago', 4, _utf8mb4'Mansión abandonada donde ocurren sucesos paranormales.', '2000-01-01', 3, 3, 3, 'https://placehold.co/300x300', _utf8mb4'Investigaciones Paranormales'), 
(11, _utf8mb4'El Carreta sin Bueyes', 6, _utf8mb4'Se dice que una carreta fantasma se aparece en las noches de luna llena.', '1780-01-01', 5, 5, 5, 'https://placehold.co/300x300', _utf8mb4'Narraciones Rurales'), 
(12, _utf8mb4'La Siguanaba', 4, _utf8mb4'Mujer con rostro de calavera que castiga a los hombres infieles.', '1820-01-01', 4, 4, 4, 'https://placehold.co/300x300', _utf8mb4'Historias de la Abuela');
